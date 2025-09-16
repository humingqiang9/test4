import kotlinx.coroutines.*

fun main() = runBlocking {
    val networkService = NetworkService()
    val url = "https://httpbin.org/get" // Using a test API endpoint

    println("Starting network request to $url")

    val response = networkService.fetchData(url)

    if (response != null) {
        println("Response received:")
        println(response)
    } else {
        println("Failed to get a response.")
    }
}