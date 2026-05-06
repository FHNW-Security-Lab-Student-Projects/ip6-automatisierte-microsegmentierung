import { render } from "./render.js";
import { addNode } from "./nodes.js";
import { addSwitch } from "./switches.js";
import { addGroup } from "./groups.js";
import { addRule } from "./rules.js";
import { attachNodeToSwitch } from "./attachments.js";
import { connectSwitches } from "./switches.js";

import { downloadJSON, importJSON } from "./export.js";

document.getElementById("nodeForm").addEventListener("submit", (e) => {
	e.preventDefault();

	const input = document.getElementById("nodeName");

	addNode(input.value.trim());

	input.value = "";

	input.focus();
});

document.getElementById("switchForm").addEventListener("submit", (e) => {
	e.preventDefault();

	const input = document.getElementById("switchName");

	addSwitch(input.value.trim());

	input.value = "";

	input.focus();
});

document.getElementById("groupForm").addEventListener("submit", (e) => {
	e.preventDefault();

	const name = document.getElementById("groupName").value.trim();

	const checkboxes = document.querySelectorAll(
		"#groupMembers input[type='checkbox']",
	);

	const members = [];

	checkboxes.forEach((cb) => {
		if (cb.checked) {
			members.push(cb.value);
		}
	});

	addGroup(name, members);

	document.getElementById("groupName").value = "";
});

document.getElementById("attachForm").addEventListener("submit", (e) => {
	e.preventDefault();

	const node = document.getElementById("attachNode").value;

	const sw = document.getElementById("attachSwitch").value;

	attachNodeToSwitch(node, sw);
});

document.getElementById("ruleForm").addEventListener("submit", (e) => {
	e.preventDefault();

	const type = document.getElementById("ruleType").value;

	const src = document.getElementById("ruleSrc").value;

	const dst = document.getElementById("ruleDst").value;

	addRule(type, src, dst);
});

document.getElementById("downloadBtn").addEventListener("click", downloadJSON);

document
	.getElementById("switchConnectionForm")
	.addEventListener("submit", (e) => {
		e.preventDefault();

		const switchA = document.getElementById("switchA").value;

		const switchB = document.getElementById("switchB").value;

		connectSwitches(switchA, switchB);
	});

document.getElementById("copyJsonBtn").addEventListener("click", async () => {
	const preview = document.getElementById("jsonPreview");

	try {
		await navigator.clipboard.writeText(preview.textContent);

		alert("JSON copied to clipboard");
	} catch (err) {
		console.error(err);

		alert("Failed to copy JSON");
	}
});

document.getElementById("importFile").addEventListener("change", async (e) => {
	const file = e.target.files[0];

	if (!file) return;

	try {
		const text = await file.text();

		const json = JSON.parse(text);

		importJSON(json);

		render();

		alert("JSON imported successfully");
	} catch (err) {
		console.error(err);

		alert("Invalid JSON file");
	}
});

render();
