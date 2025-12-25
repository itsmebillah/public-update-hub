const GAS_URL =
  "https://script.google.com/macros/s/AKfycbwM263dREny57y2nXBCrAvgesWLdITWPHJLjqv2NmALXkCMIK016bZ819bMwzX0hn4t2g/exec";

const grid = document.getElementById("projectsGrid");

fetch(`${GAS_URL}?action=projects`)
  .then(res => res.json())
  .then(json => {
    grid.innerHTML = "";

    if (!json.success || json.data.length === 0) {
      grid.innerHTML = "<p>No projects found.</p>";
      return;
    }

    json.data.forEach(p => {
      const card = document.createElement("div");
      card.className = "project-card";

      card.innerHTML = `
        <h3>${p.title}</h3>
        <p>${p.description || ""}</p>
        ${p.link ? `<a href="${p.link}" target="_blank">View Project →</a>` : ""}
      `;

      grid.appendChild(card);
    });
  })
  .catch(err => {
    grid.innerHTML = "<p>Error loading projects</p>";
    console.error(err);
  });
