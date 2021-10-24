import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:simple_shop_provider/cart/cartprovider.dart';
import 'package:simple_shop_provider/cart/item.dart';

class CartPage extends StatelessWidget {
  const CartPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Cart"),
      ),
      body: Consumer<CartProvider>(
        builder: (context, cartProvider, child) => ListView.builder(
            itemBuilder: (context, index) {
              final Item item = cartProvider.itemCart[index];
              return InkWell(
                child: Card(
                  child: Container(
                    padding: const EdgeInsets.all(15),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text(item.name),
                        Text("\$" + item.price.toString()),
                      ],
                    ),
                  ),
                ),
              );
            },
            itemCount: cartProvider.itemCart.length),
      ),
      bottomSheet: Consumer<CartProvider>(
        builder: (context, cartProvider, child) => Container(
          padding: const EdgeInsets.all(10),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  const Text(
                    "Total :",
                    style: TextStyle(
                      fontSize: 20,
                    ),
                  ),
                  const SizedBox(
                    width: 10,
                  ),
                  Text(
                    cartProvider.getTotalPrice().toString(),
                    style: const TextStyle(
                      fontSize: 36,
                    ),
                  ),
                ],
              ),
              TextButton(
                  onPressed: () {
                    const snackBar = SnackBar(
                      content: Text('Item checked out'),
                    );

                    // Find the ScaffoldMessenger in the widget tree
                    // and use it to show a SnackBar.
                    ScaffoldMessenger.of(context).showSnackBar(snackBar);
                  },
                  child: const Text("Checkout")),
            ],
          ),
        ),
      ),
    );
  }
}
