import { Component, OnInit } from '@angular/core';
import { DataServiceAnX44HuDPuTo, DataItem } from './services/data-service-anX44HuDPuTo';

@Component({
  selector: 'app-root',
  template: `
    <h1>Данные из API</h1>
    <ul>
      <li *ngFor="let item of dataItems">
        {{ item.id }}: {{ item.name }} - {{ item.description }}
      </li>
    </ul>
  `,
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  dataItems: DataItem[] = [];

  constructor(private dataService: DataServiceAnX44HuDPuTo) {}

  ngOnInit(): void {
    this.dataService.getData().subscribe(
      (data) => {
        // Преобразуем данные в нужный формат, если необходимо
        this.dataItems = data.slice(0, 5).map(item => ({
          id: item.id,
          name: item.title,
          description: item.body
        }));
      },
      (error) => {
        console.error('Ошибка при получении данных:', error);
      }
    );
  }
}