import 'dart:io';
import 'dart:convert';
import 'dart:math';

/// Generates a random string of the specified length.
String _generateRandomName(int length) {
  final random = Random();
  const characters = 'abcdefghijklmnopqrstuvwxyz0123456789';
  return List.generate(length, (index) => characters[random.nextInt(characters.length)]).join();
}

/// Fetches data from a URL and saves it to a file with a random name.
Future<void> fetchAndSaveData() async {
  final url = 'http://example.com/data.json';
  final randomFileName = 'data_${_generateRandomName(8)}.dart';
  final filePath = '/workspace/dart_project/$randomFileName';

  try {
    final httpClient = HttpClient();
    final request = await httpClient.getUrl(Uri.parse(url));
    final response = await request.close();

    if (response.statusCode == HttpStatus.ok) {
      final responseBody = await response.transform(utf8.decoder).join();
      final file = File(filePath);
      await file.writeAsString('const fetchedData = \'\'\'\n$responseBody\n\'\'\';\n');
      print('Data saved to $filePath');
    } else {
      print('Failed to fetch data. Status code: ${response.statusCode}');
    }
  } catch (error) {
    print('Error occurred: $error');
  }
}

void main() async {
  await fetchAndSaveData();
}