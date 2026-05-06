import { network } from "./state.js";
import { render } from "./render.js";

export function addGroup(name, members) {
	if (!name) return;

	const exists = network.groups.some((g) => g.name === name);

	if (exists) {
		alert("Group already exists");
		return;
	}

	network.groups.push({
		name,
		members,
	});

	render();
}

export function deleteGroup(index) {
	const groupName = network.groups[index].name;

	network.groups.splice(index, 1);

	network.constraints = network.constraints.filter((c) => {
		if (c.src === groupName || c.dst === groupName) {
			return false;
		}

		return true;
	});

	render();
}
