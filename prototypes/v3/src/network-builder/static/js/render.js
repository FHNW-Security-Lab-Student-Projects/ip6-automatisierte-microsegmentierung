import { network } from "./state.js";

import { deleteNode } from "./nodes.js";
import { deleteSwitch, deleteSwitchConnection } from "./switches.js";
import { deleteGroup } from "./groups.js";
import { deleteRule } from "./rules.js";
import { deleteAttachment } from "./attachments.js";

export function render() {
	renderNodes();
	renderSwitches();

	renderSwitchConnectionSelectors();
	renderSwitchConnections();

	renderGroupMembers();
	renderGroups();

	renderSelectors();
	renderAttachments();

	renderRuleSelectors();
	renderRules();

	renderJSONPreview();
}

function renderJSONPreview() {
	const preview = document.getElementById("jsonPreview");

	preview.textContent = JSON.stringify(network, null, 4);
}

function renderNodes() {
	const list = document.getElementById("nodeList");

	list.innerHTML = "";

	network.nodes.forEach((node, index) => {
		const li = document.createElement("li");

		li.textContent = node + " ";

		const btn = document.createElement("button");

		btn.textContent = "Delete";

		btn.onclick = () => deleteNode(index);

		li.appendChild(btn);

		list.appendChild(li);
	});
}

function renderSwitches() {
	const list = document.getElementById("switchList");

	list.innerHTML = "";

	network.switches.forEach((sw, index) => {
		const li = document.createElement("li");

		li.textContent = sw + " ";

		const btn = document.createElement("button");

		btn.textContent = "Delete";

		btn.onclick = () => deleteSwitch(index);

		li.appendChild(btn);

		list.appendChild(li);
	});
}

function renderGroupMembers() {
	const container = document.getElementById("groupMembers");

	container.innerHTML = "";

	network.nodes.forEach((node) => {
		const label = document.createElement("label");

		const checkbox = document.createElement("input");

		checkbox.type = "checkbox";

		checkbox.value = node;

		label.appendChild(checkbox);

		label.appendChild(document.createTextNode(" " + node));

		container.appendChild(label);

		container.appendChild(document.createElement("br"));
	});
}

function renderGroups() {
	const list = document.getElementById("groupList");

	list.innerHTML = "";

	network.groups.forEach((group, index) => {
		const li = document.createElement("li");

		li.textContent = `${group.name}: ${group.members.join(", ")} `;

		const btn = document.createElement("button");

		btn.textContent = "Delete";

		btn.onclick = () => deleteGroup(index);

		li.appendChild(btn);

		list.appendChild(li);
	});
}

function renderSelectors() {
	const nodeSelect = document.getElementById("attachNode");

	const switchSelect = document.getElementById("attachSwitch");

	nodeSelect.innerHTML = "";
	switchSelect.innerHTML = "";

	network.nodes.forEach((node) => {
		const option = document.createElement("option");

		option.value = node;
		option.textContent = node;

		nodeSelect.appendChild(option);
	});

	network.switches.forEach((sw) => {
		const option = document.createElement("option");

		option.value = sw;
		option.textContent = sw;

		switchSelect.appendChild(option);
	});
}

function renderAttachments() {
	const list = document.getElementById("attachmentList");

	list.innerHTML = "";

	network.constraints
		.filter((c) => c.type === "LOCATED_AT")
		.forEach((c) => {
			const li = document.createElement("li");

			li.textContent = `${c.node} -> ${c.switch} `;

			const btn = document.createElement("button");

			btn.textContent = "Delete";

			btn.onclick = () => deleteAttachment(c);

			li.appendChild(btn);

			list.appendChild(li);
		});
}

function renderRuleSelectors() {
	const srcSelect = document.getElementById("ruleSrc");

	const dstSelect = document.getElementById("ruleDst");

	srcSelect.innerHTML = "";
	dstSelect.innerHTML = "";

	const entities = [...network.nodes, ...network.groups.map((g) => g.name)];

	entities.forEach((entity) => {
		const srcOption = document.createElement("option");

		srcOption.value = entity;
		srcOption.textContent = entity;

		srcSelect.appendChild(srcOption);

		const dstOption = document.createElement("option");

		dstOption.value = entity;
		dstOption.textContent = entity;

		dstSelect.appendChild(dstOption);
	});
}

function renderRules() {
	const list = document.getElementById("ruleList");

	list.innerHTML = "";

	network.constraints
		.filter((c) => c.type === "ALLOW" || c.type === "DENY")
		.forEach((rule) => {
			const li = document.createElement("li");

			li.textContent = `${rule.type}: ${rule.src} -> ${rule.dst} `;

			const btn = document.createElement("button");

			btn.textContent = "Delete";

			btn.onclick = () => deleteRule(rule);

			li.appendChild(btn);

			list.appendChild(li);
		});
}

function renderSwitchConnectionSelectors() {
	const switchA = document.getElementById("switchA");

	const switchB = document.getElementById("switchB");

	switchA.innerHTML = "";
	switchB.innerHTML = "";

	network.switches.forEach((sw) => {
		const optionA = document.createElement("option");

		optionA.value = sw;
		optionA.textContent = sw;

		switchA.appendChild(optionA);

		const optionB = document.createElement("option");

		optionB.value = sw;
		optionB.textContent = sw;

		switchB.appendChild(optionB);
	});
}

function renderSwitchConnections() {
	const list = document.getElementById("switchConnectionList");

	list.innerHTML = "";

	network.constraints
		.filter((c) => c.type === "CONNECTED")
		.forEach((c) => {
			const li = document.createElement("li");

			li.textContent = `${c.node_a} <-> ${c.node_b}`;

			const btn = document.createElement("button");

			btn.textContent = "Delete";

			btn.onclick = () => deleteSwitchConnection(c);

			li.appendChild(btn);

			list.appendChild(li);
		});
}
