using Microsoft.AspNetCore.Mvc;
using System.Collections.Generic;
using System.Linq;

namespace MyWebApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ItemsController : ControllerBase
    {
        // In-memory list to simulate a database
        private static List<Item> items = new List<Item>
        {
            new Item { Id = 1, Name = "Laptop", Description = "Gaming Laptop" },
            new Item { Id = 2, Name = "Phone", Description = "Smartphone" },
            new Item { Id = 3, Name = "Tablet", Description = "Drawing Tablet" }
        };

        // GET: api/items
        [HttpGet]
        public ActionResult<IEnumerable<Item>> GetItems()
        {
            return Ok(items);
        }

        // GET: api/items/5
        [HttpGet("{id}")]
        public ActionResult<Item> GetItem(int id)
        {
            var item = items.FirstOrDefault(i => i.Id == id);
            if (item == null)
            {
                return NotFound();
            }
            return Ok(item);
        }

        // POST: api/items
        [HttpPost]
        public ActionResult<Item> CreateItem(Item newItem)
        {
            // Generate a new ID
            newItem.Id = items.Max(i => i.Id) + 1;
            items.Add(newItem);
            
            return CreatedAtAction(nameof(GetItem), new { id = newItem.Id }, newItem);
        }

        // PUT: api/items/5
        [HttpPut("{id}")]
        public IActionResult UpdateItem(int id, Item updatedItem)
        {
            var existingItem = items.FirstOrDefault(i => i.Id == id);
            if (existingItem == null)
            {
                return NotFound();
            }

            existingItem.Name = updatedItem.Name;
            existingItem.Description = updatedItem.Description;
            
            return NoContent();
        }

        // DELETE: api/items/5
        [HttpDelete("{id}")]
        public IActionResult DeleteItem(int id)
        {
            var item = items.FirstOrDefault(i => i.Id == id);
            if (item == null)
            {
                return NotFound();
            }

            items.Remove(item);
            return NoContent();
        }
    }

    public class Item
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
    }
}