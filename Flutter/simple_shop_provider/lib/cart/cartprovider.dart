import 'package:flutter/material.dart';
import 'package:simple_shop_provider/cart/item.dart';

class CartProvider extends ChangeNotifier {
  List<Item> itemCart = [];

  void addItemCart(String id, String name, int price) {
    itemCart.add(Item(id, name, price));
    notifyListeners();
  }

  void delItemCart(String id) {
    itemCart.removeWhere((element) => element.id == id);
  }

  int getTotalPrice() {
    return itemCart.fold(0, (previous, current) => previous + current.price);
  }

}