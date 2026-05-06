import { network } from "./state.js";
import { render } from "./render.js";

export function addSwitch(name) {
	if (!name) return;

	if (network.switches.includes(name)) {
		alert("Switch already exists");
		return;
	}

	network.switches.push(name);

	render();
}

export function deleteSwitch(index) {
	const switchName = network.switches[index];

	network.switches.splice(index, 1);

	network.constraints = network.constraints.filter((c) => {
		if (c.switch === switchName) {
			return false;
		}

		if (c.node_a === switchName || c.node_b === switchName) {
			return false;
		}

		return true;
	});

	render();
}

export function connectSwitches(nodeA, nodeB) {
	if (nodeA === nodeB) {
		alert("Cannot connect switch to itself");
		return;
	}

	const exists = network.constraints.some(
		(c) =>
			c.type === "CONNECTED" &&
			((c.node_a === nodeA && c.node_b === nodeB) ||
				(c.node_a === nodeB && c.node_b === nodeA)),
	);

	if (exists) {
		alert("Connection already exists");
		return;
	}

	network.constraints.push({
		type: "CONNECTED",
		node_a: nodeA,
		node_b: nodeB,
	});

	render();
}

export function deleteSwitchConnection(connectionToDelete) {
	network.constraints = network.constraints.filter(
		(c) => c !== connectionToDelete,
	);

	render();
}
