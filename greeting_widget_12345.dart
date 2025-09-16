import 'package:flutter/material.dart';

class GreetingWidget extends StatelessWidget {
  final String greeting;

  const GreetingWidget({Key? key, required this.greeting}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Card(
        elevation: 4,
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Text(
            greeting,
            style: Theme.of(context).textTheme.headlineMedium?.copyWith(
                  color: Colors.blue,
                  fontWeight: FontWeight.bold,
                ),
            textAlign: TextAlign.center,
          ),
        ),
      ),
    );
  }
}