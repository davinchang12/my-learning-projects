import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:simple_shop_provider/cart/cartprovider.dart';
import 'package:simple_shop_provider/cart/item.dart';
import 'package:simple_shop_provider/screen/cartpage.dart';

int itemCount = Item.itemShop.length;
List<bool> _checked = <bool>[];

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {

  @override
  void initState() {
    for(var i = 0; i < itemCount; i++) {
      _checked.add(false);
    }
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    CartProvider cartProvider = Provider.of<CartProvider>(context, listen: false);
    return Scaffold(
      appBar: AppBar(
        title: const Text('Simple Shop Provider'),
        actions: [
          IconButton(
            onPressed: () {
              Navigator.push(
                  context, MaterialPageRoute(builder: (context) => const CartPage()));
            },
            icon: const Icon(Icons.shopping_cart),
          ),
        ],
        backgroundColor: Colors.blue,
      ),
      body: ListView.builder(
        itemBuilder: (context, index) {
          final Item item = Item.itemShop[index];
          return InkWell(
            child: Card(
              child: Container(
                padding: const EdgeInsets.only(left: 10, right: 10),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(item.name),
                    Text("\$" + item.price.toString()),
                    IconButton(
                      icon: _checked.elementAt(index) ? const Icon(Icons.check) : const Icon(Icons.add),
                      onPressed: () {
                        setState(() {
                          if (_checked[index] == true) {
                            cartProvider.delItemCart(item.id);
                          } else {
                            cartProvider.addItemCart(item.id, item.name, item.price);
                          }

                          _checked[index] = !_checked.elementAt(index);
                        });
                      },
                    ),
                  ],
                ),
              ),
            ),
          );
        },
        itemCount: itemCount
      ),
    );
  }
}
