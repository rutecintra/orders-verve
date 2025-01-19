import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CurrencyPipe } from '@angular/common';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

interface Item {
  name: string;
  sku: string;
  image: string;
  quantity: number;
  maxQuantity: number;
}

interface Order {
  id: string;
  orderId: string;
  createdDate: string;
  status: string;
  totalAmount: number;
  commissionFees: number;
  shippingCharges: number;
  invoiceUrl: string;
  invoiceName: string;
  customerName: string;
  customerLanguage: string;
  shippingAddress: string;
  items: Item[];
}

@Component({
  selector: 'app-order-details',
  imports: [
    CurrencyPipe,
    CommonModule,
    RouterLink
  ],
  templateUrl: './order-details.component.html',
  styleUrl: './order-details.component.css'
})
export class OrderDetailsComponent implements OnInit {
  order!: Order;

  constructor(private route: ActivatedRoute) {}

  ngOnInit() {
    const orderId = this.route.snapshot.paramMap.get('id');

    this.order = {
      id: orderId || '1',
      orderId: 'EC000107973',
      createdDate: '2025-01-18T21:46:00',
      status: 'Awaiting shipment',
      totalAmount: 44.02,
      commissionFees: 6.90,
      shippingCharges: 0.00,
      invoiceUrl: 'assets/delivery-invoice.pdf',
      invoiceName: 'delivery-EC000107973.pdf',
      customerName: 'Tiendamia Marketplace',
      customerLanguage: 'English - US',
      shippingAddress: '8404 NW 90TH ST UNIT 300TH',
      items: [
        {
          name: 'Happy Clinique For Women Eau De Parfum Spray 3.4 oz',
          sku: '413912',
          image: 'https://acdn.mitiendanube.com/stores/001/167/965/products/cliniquehappy-c75eb6120cba0d0f7c17141601995011-1024-1024.jpg',
          quantity: 1,
          maxQuantity: 1
        }
      ]
    };
  }
}
