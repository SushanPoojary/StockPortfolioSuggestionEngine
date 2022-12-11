/*!

=========================================================
* Material Dashboard React - v1.8.0
=========================================================

* Product Page: https://www.creative-tim.com/product/material-dashboard-react
* Copyright 2019 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/material-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
// @material-ui/icons

import ShowChart from "@material-ui/icons/ShowChart";
import HomeSharp from "@material-ui/icons/HomeSharp";
import DashboardPage from "views/Dashboard/Dashboard.js";
import UserProfile from "views/UserProfile/UserProfile.js";


const dashboardRoutes = [
  {
    path: "/user",
    name: "Dashboard",
    icon: HomeSharp,
    component: UserProfile,
    layout: "/admin"
  },
  {
    path: "/dashboard",
    name: "Investment Details",
    icon: ShowChart,
    component: DashboardPage,
    layout: "/admin"
  }
];

export default dashboardRoutes;
