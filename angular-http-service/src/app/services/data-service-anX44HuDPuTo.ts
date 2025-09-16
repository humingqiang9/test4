import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// Интерфейс для типизации данных
export interface DataItem {
  id: number;
  name: string;
  description: string;
}

@Injectable({
  providedIn: 'root'
})
export class DataServiceAnX44HuDPuTo {
  private apiUrl = 'https://jsonplaceholder.typicode.com/posts'; // Пример API

  constructor(private http: HttpClient) { }

  // Получение всех данных
  getData(): Observable<DataItem[]> {
    return this.http.get<DataItem[]>(this.apiUrl);
  }

  // Получение данных по ID
  getDataById(id: number): Observable<DataItem> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.get<DataItem>(url);
  }

  // Создание новой записи
  createData(item: DataItem): Observable<DataItem> {
    return this.http.post<DataItem>(this.apiUrl, item);
  }

  // Обновление записи
  updateData(id: number, item: DataItem): Observable<DataItem> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.put<DataItem>(url, item);
  }

  // Удаление записи
  deleteData(id: number): Observable<void> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.delete<void>(url);
  }
}