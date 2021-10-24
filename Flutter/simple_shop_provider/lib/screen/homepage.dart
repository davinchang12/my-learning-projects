import 'package:flutter/material.dart';
import 'package:simple_shop_provider/cart/item.dart';
import 'package:simple_shop_provider/screen/cartpage.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Simple Shop Provider'),
        actions: [
          IconButton(
            onPressed: () {
              Navigator.push(
                  context, MaterialPageRoute(builder: (context) => CartPage()));
            },
            icon: const Icon(Icons.shopping_cart),
          ),
        ],
        backgroundColor: Colors.blue,
      ),
      body: ListView.builder(
        itemBuilder: (context, index) {
          final Item item = Item.itemShop[index];
          bool _checked = false;
          return InkWell(
            child: Card(
              child: Container(
                padding: const EdgeInsets.only(left: 10, right: 10),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(item.name),
                    Text(item.price.toString()),
                    IconButton(
                      icon: _checked ? Icon(Icons.check) : Icon(Icons.add),
                      onPressed: () {
                        setState(() {
                          _checked = !_checked;
                        });
                      },
                    ),
                  ],
                ),
              ),
            ),
          );
        },
        itemCount: Item.itemShop.length,
      ),
    );
  }
}
