class Navbar extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
        <header>
            <nav class="nav-bar">
                <div class="logo">
                    <h1>Logo</h1>
                </div>
    
                <div class="nav-list">
                    <ul>
                        <li class="nav-item"><a href="#" class="nav-link">Início</a></li>
                        <li class="nav-item"><a href="#" class="nav-link">Tópicos</a></li>
                        <li class="nav-item"><a href="#" class="nav-link">Sobre Nós</a></li>
                    </ul>
                </div>
    
                <div class="mobile-menu-icon">
                    <button onclick="menuShow()"><img class="icon" src="app/view/imgs/list.svg" alt="menu"></button>
                </div>
            </nav>
    
            <div class="mobile-menu">
                <ul>
                    <li class="nav-item"><a href="#" class="nav-link">Início</a></li>
                    <li class="nav-item"><a href="#" class="nav-link">Tópicos</a></li>
                    <li class="nav-item"><a href="#" class="nav-link">Sobre Nós</a></li>
                </ul>
            </div>
        </header>`;
  }
}

customElements.define("custom-navbar", Navbar);
