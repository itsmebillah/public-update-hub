const API = "https://script.google.com/macros/s/AKfycbwM263dREny57y2nXBCrAvgesWLdITWPHJLjqv2NmALXkCMIK016bZ819bMwzX0hn4t2g/exec";

fetch(`${API}?action=getArticles`)
.then(r => r.json())
.then(res => {
  const box = document.getElementById("articles");
  box.innerHTML = res.data.map(a => `
    <div class="card">
      <h3>${a.title}</h3>
      <p>${a.short}</p>
      <a href="article.html?slug=${a.slug}">Read</a>
    </div>
  `).join("");
});
