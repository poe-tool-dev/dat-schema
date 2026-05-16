import * as d3 from 'd3';
import { ValidFor, type SchemaTable } from './types.js';

type Node = {
  id: string;
  group: ValidFor;
  details: SchemaTable;
  x: number;
  y: number;
  expanded: boolean;
};

type Link = {
  source: Node | string;
  target: Node | string;
  index?: number;
};

let allTables: SchemaTable[] = [];
let gameVersion: ValidFor = ValidFor.PoE1;

const graphContainer = document.getElementById('graph-container');
const btnPoE1 = document.getElementById('poe1-btn');
const btnPoE2 = document.getElementById('poe2-btn');
const btnRecenter = document.getElementById('recenter-btn');
const inputSearch = document.getElementById('search-input') as HTMLInputElement;
const btnClearSearch = document.getElementById('search-clear');
const depthSlider = document.getElementById('depth-slider') as HTMLInputElement;
const depthVal = document.getElementById('depth-val');

let relationDepth = 1;
let currentRootNode: Node | null = null;

if (depthSlider && depthVal) {
  depthSlider.addEventListener('input', (e) => {
    relationDepth = parseInt((e.target as HTMLInputElement).value, 10);
    depthVal.textContent = relationDepth.toString();
  });
}

const measureCanvas = document.createElement('canvas');
const measureContext = measureCanvas.getContext('2d');
if (measureContext) {
  measureContext.font = '11px monospace';
}

btnPoE1?.addEventListener('click', () => {
  gameVersion = ValidFor.PoE1;
  btnPoE1.classList.add('active');
  btnPoE2?.classList.remove('active');
  render();
});

btnPoE2?.addEventListener('click', () => {
  gameVersion = ValidFor.PoE2;
  btnPoE2.classList.add('active');
  btnPoE1?.classList.remove('active');
  render();
});

function render() {
  if (!graphContainer) return;
  const filteredTables = allTables.filter(
    (t) => t.validFor === gameVersion || t.validFor === ValidFor.Common,
  );
  graphContainer.innerHTML = '';

  const width = graphContainer.clientWidth;
  const height = graphContainer.clientHeight;

  const nodes: Node[] = filteredTables.map((table) => ({
    id: table.name,
    group: table.validFor,
    details: table,
    x: width / 2 + (Math.random() - 0.5) * (Math.min(width, height) * 0.8),
    y: height / 2 + (Math.random() - 0.5) * (Math.min(width, height) * 0.8),
    expanded: false,
  }));

  const nodeMap = new Map(nodes.map((n) => [n.id, n]));
  const allLinks: Link[] = [];
  filteredTables.forEach((table) => {
    table.columns.forEach((col) => {
      if (col.references) {
        const targetName = col.references.table;
        if (nodeMap.has(targetName)) {
          allLinks.push({
            source: table.name,
            target: targetName,
          });
        }
      }
    });
  });

  let currentNodes: Node[] = [...nodes];
  let currentLinks: Link[] = [...allLinks];

  const svg = d3
    .select(graphContainer)
    .append('svg')
    .attr('viewBox', [0, 0, width, height])
    .attr('width', '100%')
    .attr('height', '100%');

  const g = svg.append('g');

  const zoom = d3
    .zoom<SVGSVGElement, unknown>()
    .scaleExtent([0.1, 4])
    .filter((event) => !event.shiftKey && !event.ctrlKey && !event.button)
    .on('zoom', (event) => g.attr('transform', event.transform));

  svg.call(zoom);

  const linkGroup = g.append('g').attr('class', 'links');
  const nodeGroup = g.append('g').attr('class', 'nodes');

  const simulation = d3
    .forceSimulation(currentNodes)
    .force('charge', d3.forceManyBody().strength(-300))
    .force('center', d3.forceCenter(width / 2, height / 2))
    .force('collide', d3.forceCollide().radius(30));

  svg.on('click', (event: MouseEvent) => {
    if (event.shiftKey) return;
    currentRootNode = null;
    currentNodes = [...nodes];
    currentLinks = [...allLinks];
    draw(currentNodes, allLinks);
  });

  if (depthSlider && depthVal) {
    depthSlider.oninput = (e) => {
      relationDepth = parseInt((e.target as HTMLInputElement).value, 10);
      depthVal.textContent = relationDepth.toString();
      if (currentRootNode) isolate(currentRootNode);
    };
  }

  if (btnRecenter) {
    btnRecenter.onclick = () => {
      svg.transition().duration(750).call(zoom.transform, d3.zoomIdentity);
    };
  }

  if (btnClearSearch) {
    btnClearSearch.onclick = () => {
      if (inputSearch) {
        inputSearch.value = '';
        inputSearch.focus();
        applySearchState();
      }
    };
  }

  if (inputSearch) {
    inputSearch.addEventListener('input', applySearchState);
  }

  draw(currentNodes, allLinks);

  function dragStart(
    event: d3.D3DragEvent<SVGSVGElement, Node, d3.SimulationNodeDatum>,
  ) {
    simulation.stop();
    event.subject.fx = event.subject.x;
    event.subject.fy = event.subject.y;
  }

  function dragMove(
    event: d3.D3DragEvent<SVGSVGElement, Node, d3.SimulationNodeDatum>,
  ) {
    event.subject.fx = event.x;
    event.subject.fy = event.y;
    event.subject.x = event.x;
    event.subject.y = event.y;
    updatePositions();
  }

  function updatePositions() {
    linkGroup
      .selectAll<SVGLineElement, Link>('line')
      .attr('x1', (d: Link) => (typeof d.source === 'object' ? d.source.x : 0))
      .attr('y1', (d: Link) => (typeof d.source === 'object' ? d.source.y : 0))
      .attr('x2', (d: Link) => (typeof d.target === 'object' ? d.target.x : 0))
      .attr('y2', (d: Link) => (typeof d.target === 'object' ? d.target.y : 0));
    nodeGroup
      .selectAll<SVGGElement, Node>('g.node')
      .attr('transform', (d: Node) => `translate(${d.x},${d.y})`);
  }

  function isolate(d: Node) {
    currentRootNode = d;
    nodeGroup.selectAll('g.node').style('opacity', 1);
    linkGroup.selectAll('line').style('opacity', 0.4);

    const neighbors = new Set<string>();

    const queue: { id: string; depth: number }[] = [{ id: d.id, depth: 0 }];
    neighbors.add(d.id);

    let head = 0;
    while (head < queue.length) {
      const current = queue[head++];
      if (current.depth >= relationDepth) continue;

      allLinks.forEach((l) => {
        const s = typeof l.source === 'object' ? l.source.id : l.source;
        const t = typeof l.target === 'object' ? l.target.id : l.target;

        let nextId: string | null = null;
        if (s === current.id) nextId = t;
        if (t === current.id) nextId = s;

        if (nextId && !neighbors.has(nextId)) {
          neighbors.add(nextId);
          queue.push({ id: nextId, depth: current.depth + 1 });
        }
      });
    }

    currentNodes = nodes.filter((n) => neighbors.has(n.id));
    currentLinks = allLinks.filter((l) => {
      const s = typeof l.source === 'object' ? l.source.id : l.source;
      const t = typeof l.target === 'object' ? l.target.id : l.target;
      return neighbors.has(s) && neighbors.has(t);
    });

    draw(currentNodes, currentLinks);
  }

  function applySearchState() {
    const term =
      inputSearch && inputSearch.value ? inputSearch.value.toLowerCase() : '';

    if (btnClearSearch) {
      btnClearSearch.style.visibility = term ? 'visible' : 'hidden';
    }

    if (term) {
      nodeGroup
        .selectAll<SVGGElement, Node>('g.node')
        .style('opacity', (n) => (n.id.toLowerCase().includes(term) ? 1 : 0.1));
      linkGroup.selectAll('line').style('opacity', 0.05);
    } else {
      nodeGroup.selectAll('g.node').style('opacity', 1);
      linkGroup.selectAll('line').style('opacity', 0.4);
    }
  }

  function draw(simNodes: Node[], simLinks: Link[]) {
    simulation.nodes(simNodes);
    simulation.force(
      'link',
      d3
        .forceLink<Node, Link>(simLinks)
        .id((d) => d.id)
        .distance(150),
    );
    simulation.alpha(1).restart();

    const link = linkGroup
      .selectAll<SVGLineElement, Link>('line')
      .data(
        simLinks,
        (d: Link) =>
          `${typeof d.source === 'object' ? d.source.id : d.source}-${typeof d.target === 'object' ? d.target.id : d.target}`,
      );

    link.exit().remove();
    link
      .enter()
      .append('line')
      .attr('stroke', '#555')
      .attr('stroke-opacity', 0.4)
      .attr('stroke-width', 1);

    const node = nodeGroup
      .selectAll<SVGGElement, Node>('g.node')
      .data(simNodes, (d: Node) => d.id);

    node.exit().remove();

    const nodeEnter = node
      .enter()
      .append('g')
      .attr('class', 'node')
      .attr('cursor', 'grab')
      .call(
        d3
          .drag<SVGGElement, Node>()
          .filter((event) => !event.shiftKey && !event.button)
          .on('start', dragStart)
          .on('drag', dragMove),
      );

    nodeEnter
      .append('circle')
      .attr('r', 6)
      .attr('fill', '#4a9eff')
      .attr('stroke', '#222')
      .attr('stroke-width', 1.5);

    nodeEnter
      .append('text')
      .text((d: Node) => d.id)
      .attr('x', 10)
      .attr('y', 4)
      .attr('fill', '#bbb')
      .style('font-size', '10px')
      .style('font-family', 'monospace')
      .style('pointer-events', 'none');

    nodeEnter
      .on('mouseover', (_, d: Node) => {
        const neighbors = new Set<string>();
        neighbors.add(d.id);
        currentLinks.forEach((l) => {
          const s = typeof l.source === 'object' ? l.source.id : l.source;
          const t = typeof l.target === 'object' ? l.target.id : l.target;
          if (s === d.id) neighbors.add(t);
          if (t === d.id) neighbors.add(s);
        });

        nodeGroup
          .selectAll<SVGGElement, Node>('g.node')
          .style('opacity', (n) => (neighbors.has(n.id) ? 1 : 0.1));
        linkGroup
          .selectAll<SVGLineElement, Link>('line')
          .style('opacity', (l) => {
            const s = typeof l.source === 'object' ? l.source.id : l.source;
            const t = typeof l.target === 'object' ? l.target.id : l.target;
            return neighbors.has(s) && neighbors.has(t) ? 0.8 : 0.05;
          });
      })
      .on('mouseout', () => {
        applySearchState();
      });

    nodeEnter.on('click', (event: MouseEvent, d: Node) => {
      event.stopPropagation();
      if (event.shiftKey) {
        const group = d3.select(event.currentTarget as SVGGElement);
        const existingDetails = group.select('.details');

        if (!existingDetails.empty()) {
          existingDetails.remove();
          return;
        }

        const validColumns = d.details.columns
          .filter((c) => c.name && c.name !== 'Unknown')
          .map((c) => c.name!);

        const showCols = validColumns.slice(0, 10);
        if (validColumns.length > 10) showCols.push('...');
        let maxWidth = 160;
        if (measureContext) {
          showCols.forEach((txt) => {
            const w = measureContext.measureText(txt).width;
            if (w + 40 > maxWidth) maxWidth = w + 40;
          });
        }

        const bgHeight = showCols.length * 14 + 16;
        const detailsGroup = group.append('g').attr('class', 'details');

        detailsGroup
          .append('rect')
          .attr('x', 15)
          .attr('y', 10)
          .attr('width', maxWidth)
          .attr('height', bgHeight)
          .attr('fill', '#1a1a1a')
          .attr('stroke', '#444')
          .attr('rx', 4);

        showCols.forEach((txt: string, i: number) => {
          detailsGroup
            .append('text')
            .text(txt)
            .attr('x', 24)
            .attr('y', 28 + i * 14)
            .attr('fill', '#bbb')
            .style('font-size', '11px')
            .style('font-family', 'monospace');
        });
        group.raise();
      } else {
        isolate(d);
      }
    });

    simulation.on('tick', updatePositions);
    applySearchState();
  }
}

(async () => {
  try {
    const response = await fetch('./schema.min.json');
    const json = await response.json();
    allTables = json.tables;
    render();
  } catch (e) {
    console.error('Failed to load schema', e);
    if (graphContainer)
      graphContainer.innerHTML = `<div style="color:red; padding: 20px;">Failed to load ./schema.min.json. Run npm generate first.</div>`;
  }
})();
