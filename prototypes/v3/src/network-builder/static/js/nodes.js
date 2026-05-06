import { network } from "./state.js";
import { render } from "./render.js";

export function addNode(name) {
	if (!name) return;

	if (network.nodes.includes(name)) {
		alert("Node already exists");
		return;
	}

	network.nodes.push(name);

	render();
}

export function deleteNode(index) {
	const nodeName = network.nodes[index];

	network.nodes.splice(index, 1);

	// Remove from groups
	network.groups.forEach((group) => {
		group.members = group.members.filter((m) => m !== nodeName);
	});

	// Remove related constraints
	network.constraints = network.constraints.filter((c) => {
		if (c.node === nodeName) {
			return false;
		}

		if (c.src === nodeName || c.dst === nodeName) {
			return false;
		}

		return true;
	});

	render();
}
