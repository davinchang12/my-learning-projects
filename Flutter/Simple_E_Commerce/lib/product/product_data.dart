import 'package:flutter/material.dart';

class ProductData{
  String name;
  String image;
  String price;
  String desc;
  double rating;
  String stock;
  List<String> size;
  List<Color> warna;

   ProductData({
     required this.name,
     required this.image,
     required this.price,
     required this.desc,
     required this.rating,
     required this.stock,
     required this.size,
     required this.warna,
   });

   static var productDataList = 
      ProductData(
        name: "Kaos Putih Jaket Biru Background Biru", 
        image: "images/clothes1.jpg", 
        price: "Rp 80.000", 
        desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce ligula arcu, ultricies sed egestas mollis, lacinia nec diam. In nibh quam, interdum at dictum ut, porttitor eu tortor. Donec mi est, sodales sit amet metus in, malesuada porta libero. Vestibulum vitae facilisis turpis. Morbi a iaculis felis, sed feugiat sem. Vestibulum eu tincidunt tellus. Mauris nec porta metus. Fusce id sodales nisl. Sed vel nulla tempus, sodales erat sit amet, faucibus enim. Nam eget lobortis odio. Suspendisse facilisis in quam eget gravida. Duis eu odio enim.",
        rating: 4.5, 
        stock: "500",
        size: [
          "S",
          "M",
          "L",
          "XL",
          "XXL"
        ],
        warna: [
          Colors.black,
          Colors.white,
          Colors.lightBlue,
          Colors.red
        ]
      );
}