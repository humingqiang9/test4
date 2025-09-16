using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;

namespace MyWebApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class lt1NJY41QjQvController : ControllerBase
    {
        private static List<string> items = new List<string>
        {
            "Item 1",
            "Item 2",
            "Item 3"
        };

        // GET: api/lt1NJY41QjQv
        [HttpGet]
        public ActionResult<IEnumerable<string>> Get()
        {
            return Ok(items);
        }

        // GET: api/lt1NJY41QjQv/5
        [HttpGet("{id}")]
        public ActionResult<string> Get(int id)
        {
            if (id < 0 || id >= items.Count)
            {
                return NotFound();
            }
            return Ok(items[id]);
        }

        // POST: api/lt1NJY41QjQv
        [HttpPost]
        public ActionResult<string> Post([FromBody] string value)
        {
            items.Add(value);
            return CreatedAtAction(nameof(Get), new { id = items.Count - 1 }, value);
        }

        // PUT: api/lt1NJY41QjQv/5
        [HttpPut("{id}")]
        public IActionResult Put(int id, [FromBody] string value)
        {
            if (id < 0 || id >= items.Count)
            {
                return NotFound();
            }

            items[id] = value;
            return NoContent();
        }

        // DELETE: api/lt1NJY41QjQv/5
        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            if (id < 0 || id >= items.Count)
            {
                return NotFound();
            }

            items.RemoveAt(id);
            return NoContent();
        }
    }
}