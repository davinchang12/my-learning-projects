import 'package:flutter/material.dart';
import 'package:simple_shop_provider/cart/item.dart';

class CartProvider extends ChangeNotifier {
  List<Item> itemCart = [];

  void addItemCart(String id, String name, int price) {
    itemCart.add(Item(id, name, price));
    notifyListeners();
  }

  // TODO 1 : delete item cart
  void delItemCart(String id) {
    
  }
}