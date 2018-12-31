import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'finding-donors-web-app';
  public navItems = [
    {
      name: 'Home',
      url: '/home',
      icon: 'icon-home',
    },
    {
      name: 'Data Exploration',
      url: '/data-exploration',
      icon: 'icon-pencil',
    },
    // {
    //   name: 'Model Learning',
    //   url: '/model-learning',
    //   icon: 'icon-speedometer',
    // },
    // {
    //   name: 'Model Complexity',
    //   url: '/model-complexity',
    //   icon: 'icon-puzzle',
    // },
  ];

  public sidebarMinimized = true;
  private changes: MutationObserver;
  public element: HTMLElement = document.body;

  constructor() {
    this.changes = new MutationObserver((mutations) => {
      this.sidebarMinimized = document.body.classList.contains('sidebar-minimized');
    });

    this.changes.observe(<Element>this.element, {
      attributes: true
    });
  }
}
