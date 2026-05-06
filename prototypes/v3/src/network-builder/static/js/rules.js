import { network } from "./state.js";
import { render } from "./render.js";

export function addRule(type, src, dst) {
	network.constraints.push({
		type,
		src,
		dst,
	});

	render();
}

export function deleteRule(ruleToDelete) {
	network.constraints = network.constraints.filter(
		(rule) => rule !== ruleToDelete,
	);

	render();
}
