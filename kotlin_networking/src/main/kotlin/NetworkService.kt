import kotlinx.coroutines.*
import okhttp3.*
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.RequestBody.Companion.toRequestBody
import java.io.IOException

class NetworkService {
    private val client = OkHttpClient()

    suspend fun fetchData(url: String): String? {
        return withContext(Dispatchers.IO) {
            val request = Request.Builder()
                .url(url)
                .build()

            try {
                client.newCall(request).execute().use { response ->
                    if (!response.isSuccessful) {
                        println("HTTP error code: ${response.code}")
                        return@withContext null
                    }
                    response.body?.string()
                }
            } catch (e: IOException) {
                println("Network request failed: ${e.message}")
                null
            }
        }
    }
}