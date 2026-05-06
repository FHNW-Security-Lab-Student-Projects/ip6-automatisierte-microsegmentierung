import { network } from "./state.js";
import { render } from "./render.js";

export function attachNodeToSwitch(node, sw) {
	const exists = network.constraints.some(
		(c) => c.type === "LOCATED_AT" && c.node === node,
	);

	if (exists) {
		alert("Node already attached");
		return;
	}

	network.constraints.push({
		type: "LOCATED_AT",
		node,
		switch: sw,
	});

	render();
}

export function deleteAttachment(attachmentToDelete) {
	network.constraints = network.constraints.filter(
		(c) => c !== attachmentToDelete,
	);

	render();
}
