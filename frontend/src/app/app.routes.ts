import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { OrdersComponent } from './components/orders/orders.component';
import { OrderDetailsComponent } from './components/order-details/order-details.component';

export const routes: Routes = [
    {
        path: "",
        component: HomeComponent
    },
    {
        path: "home",
        component: HomeComponent
    },
    {
        path: "orders",
        component: OrdersComponent
    },
    {
        path: 'orders/:id',
        component: OrderDetailsComponent
    }
];