using Microsoft.AspNetCore.Mvc;

namespace MyApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class MYWZsDJmxBController : ControllerBase
    {
        // GET: api/MYWZsDJmxB
        [HttpGet]
        public IActionResult Get()
        {
            return Ok(new { message = "Hello from MYWZsDJmxBController!" });
        }

        // GET: api/MYWZsDJmxB/5
        [HttpGet("{id}")]
        public IActionResult Get(int id)
        {
            return Ok(new { id = id, message = $"Item with ID {id}" });
        }

        // POST: api/MYWZsDJmxB
        [HttpPost]
        public IActionResult Post([FromBody] object value)
        {
            return CreatedAtAction(nameof(Get), new { id = 1 }, value);
        }

        // PUT: api/MYWZsDJmxB/5
        [HttpPut("{id}")]
        public IActionResult Put(int id, [FromBody] object value)
        {
            return Ok(new { id = id, message = "Item updated successfully" });
        }

        // DELETE: api/MYWZsDJmxB/5
        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            return Ok(new { id = id, message = "Item deleted successfully" });
        }
    }
}