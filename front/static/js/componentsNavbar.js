class Navbar extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
       {% include 'navbar.html' %}
{% load static %}

<header>
  <nav class="nav-bar">
    <div class="logo">
      <h1>Logo</h1>
    </div>

    <div class="nav-list">
      <ul>
        <li class="nav-item">
          <a href="{% url 'index' %}" class="nav-link">Início</a>
        </li>
        <li class="nav-item">
          <a href="{% url 'analysis' %}" class="nav-link">Tópicos</a>
        </li>
        <li class="nav-item">
          <a href="{% url 'about' %}" class="nav-link">Sobre Nós</a>
        </li>
      </ul>
    </
 `;
  }
}

customElements.define("custom-navbar", Navbar);
