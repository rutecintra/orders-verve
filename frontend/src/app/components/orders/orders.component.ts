import { Component, AfterViewInit, ViewChild } from '@angular/core';
import { CurrencyPipe } from '@angular/common';
import { DatePipe } from '@angular/common';
import { NgClass } from '@angular/common';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatInputModule } from '@angular/material/input';
import { MatLabel } from '@angular/material/form-field';
import { MatFormField } from '@angular/material/form-field';
import { MatFormFieldModule } from '@angular/material/form-field';
import { FormsModule } from '@angular/forms';
import { MatSelectModule } from '@angular/material/select';
import { RouterLink } from '@angular/router';


@Component({
  selector: 'app-orders',
  imports: [
    CurrencyPipe,
    DatePipe,
    NgClass,
    MatPaginatorModule,
    MatTableModule,
    MatInputModule,
    MatLabel,
    MatFormField,
    FormsModule,
    MatFormFieldModule,
    MatSelectModule,
    RouterLink
  ],
  templateUrl: './orders.component.html',
  styleUrl: './orders.component.css'
})
export class OrdersComponent implements AfterViewInit {
  displayedColumns: string[] = ['orderId', 'status', 'items', 'quantity', 'totalAmount', 'shippingDeadline'];
  dataSource = new MatTableDataSource<Order>(ORDERS);
  filteredData = new MatTableDataSource<Order>(ORDERS);

  @ViewChild(MatPaginator) paginator!: MatPaginator;

  searchTerm: string = '';
  searchFilter: keyof Order = 'orderId';

  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
    this.filteredData.paginator = this.paginator;
  }

  applyAdvancedFilter() {
    const filterValue = this.searchTerm.toLowerCase();
  
    if (this.searchFilter && filterValue) {

      this.filteredData.data = ORDERS.filter((order) => {
        const value = order[this.searchFilter];
  
        if (Array.isArray(value)) {
          return value.some((item) =>
            item.toString().toLowerCase().includes(filterValue)
          );
        }
  
        return value?.toString().toLowerCase().includes(filterValue);
      });
    } else {
      this.filteredData.data = ORDERS;
    }
  }
}

export interface Item {
  name: string;
  sku: string;
}

export interface Order {
  id: string;
  orderId: string;
  status: string;
  items: Item[];
  quantity: number;
  totalAmount: number;
  shippingDeadline: Date;
}

const ORDERS: Order[] = [
  {
    id: '1',
    orderId: 'EC000107602',
    status: 'Awaiting',
    items: [
      { name: 'Item A', sku: 'SKU001' },
      { name: 'Item B', sku: 'SKU002' },
    ],
    quantity: 2,
    totalAmount: 35.78,
    shippingDeadline: new Date('2025-01-27T23:59:00'),
  },
  {
    id: '2',
    orderId: 'EC000107574',
    status: 'Shipped',
    items: [
      { name: 'Grampeador', sku: 'SKU001' },
      { name: 'Escova', sku: 'SKU002' },
    ],
    quantity: 2,
    totalAmount: 35.78,
    shippingDeadline: new Date('2025-01-27T23:59:00'),
  },
  {
    id: '3',
    orderId: 'EC000107553',
    status: 'Delivered',
    items: [
      { name: 'Celular Iphone', sku: 'SKU001' },
      { name: 'Shampoo', sku: 'SKU002' },
    ],
    quantity: 2,
    totalAmount: 35.78,
    shippingDeadline: new Date('2025-01-27T23:59:00'),
  }
];
