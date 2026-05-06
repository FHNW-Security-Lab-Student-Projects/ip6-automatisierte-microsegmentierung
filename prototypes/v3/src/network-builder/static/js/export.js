import { network } from "./state.js";

export function downloadJSON() {
	const data = JSON.stringify(network, null, 4);

	const blob = new Blob([data], {
		type: "application/json",
	});

	const url = URL.createObjectURL(blob);

	const a = document.createElement("a");

	a.href = url;

	a.download = "network.json";

	document.body.appendChild(a);

	a.click();

	document.body.removeChild(a);

	URL.revokeObjectURL(url);
}

export function importJSON(jsonData) {
	network.nodes = jsonData.nodes || [];

	network.switches = jsonData.switches || [];

	network.groups = jsonData.groups || [];

	network.constraints = jsonData.constraints || [];
}
