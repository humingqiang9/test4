import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'dateFormat'
})
export class DateFormatPipe implements PipeTransform {

  transform(value: any, format: string = 'shortDate'): any {
    if (!value) return '';

    const date = new Date(value);
    if (isNaN(date.getTime())) return value;

    switch (format) {
      case 'shortDate':
        return this.formatDate(date, 'MM/dd/yyyy');
      case 'longDate':
        return this.formatDate(date, 'MMMM dd, yyyy');
      case 'shortTime':
        return this.formatTime(date, 'hh:mm a');
      case 'longTime':
        return this.formatTime(date, 'hh:mm:ss a');
      case 'dateTime':
        return `${this.formatDate(date, 'MM/dd/yyyy')} ${this.formatTime(date, 'hh:mm a')}`;
      default:
        return this.formatDate(date, format);
    }
  }

  private formatDate(date: Date, format: string): string {
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    const year = date.getFullYear();

    // Simple replacement for common formats
    return format
      .replace('MM', month)
      .replace('dd', day)
      .replace('yyyy', year.toString())
      .replace('MMMM', this.getMonthName(date.getMonth()));
  }

  private formatTime(date: Date, format: string): string {
    let hours = date.getHours();
    const minutes = date.getMinutes().toString().padStart(2, '0');
    const seconds = date.getSeconds().toString().padStart(2, '0');
    
    let ampm = '';
    if (format.includes('a')) {
      ampm = hours >= 12 ? 'PM' : 'AM';
      hours = hours % 12;
      hours = hours ? hours : 12; // 0 should be 12
    }
    
    const hourStr = hours.toString().padStart(2, '0');

    return format
      .replace('hh', hourStr)
      .replace('mm', minutes)
      .replace('ss', seconds)
      .replace('a', ampm);
  }

  private getMonthName(monthIndex: number): string {
    const months = [
      'January', 'February', 'March', 'April', 'May', 'June',
      'July', 'August', 'September', 'October', 'November', 'December'
    ];
    return months[monthIndex];
  }
}