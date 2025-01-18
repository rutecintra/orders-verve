import { Component } from '@angular/core';
import { CurrencyPipe } from '@angular/common';
import { DatePipe } from '@angular/common';
import { NgClass } from '@angular/common';

@Component({
  selector: 'app-orders',
  imports: [
    CurrencyPipe,
    DatePipe,
    NgClass
  ],
  templateUrl: './orders.component.html',
  styleUrl: './orders.component.css'
})
export class OrdersComponent{
  orders = [
    {
      id: 'EC000107602-1-2765015-A',
      status: 'Awaiting shipment',
      items: 'I Love Love Moschino For Women Eau De Toilette Spray',
      quantity: 1,
      total: 35.78,
      shippingDeadline: new Date('2025-01-27T23:59:00')
    },
    {
      id: 'EC000107574-1-2764889-A',
      status: 'Awaiting shipment',
      items: 'Nautica Voyage Nautica For Men Eau De Toilette',
      quantity: 1,
      total: 26.85,
      shippingDeadline: new Date('2025-01-27T23:59:00')
    },
    {
      id: 'EC000107553-1-2764709-A',
      status: 'Canceled',
      items: 'EA Sports UFC 4 - PlayStation 4',
      quantity: 1,
      total: 0.0,
      shippingDeadline: new Date('2025-01-22T23:59:00')
    }
  ];
}
