import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-order-details',
  imports: [],
  templateUrl: './order-details.component.html',
  styleUrl: './order-details.component.css'
})
export class OrderDetailsComponent implements OnInit {
  orderId: string | null = null;

  constructor(private route: ActivatedRoute) {}

  ngOnInit(): void {
    //cath URL id
    this.orderId = this.route.snapshot.paramMap.get('id');
  }
}
