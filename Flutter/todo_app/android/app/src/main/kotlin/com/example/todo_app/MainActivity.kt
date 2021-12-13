package com.example.todo_app

import com.tekartik.sqflite.SqflitePlugin
import io.flutter.embedding.android.FlutterActivity

class MainActivity: FlutterActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        SqflitePlugin.registerWith(registrarFor("com.tekartik.sqflite.SqflitePlugin"))
    }
}