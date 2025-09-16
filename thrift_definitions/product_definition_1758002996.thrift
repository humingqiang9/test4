// Product.thrift
// Definition of a Product struct for use with Apache Thrift

namespace java com.example.thrift.product
namespace py example.thrift.product

struct Product {
  1: i32 id,
  2: string name,
  3: string description,
  4: double price,
  5: i32 quantity,
  6: optional string category,
  7: optional map<string, string> attributes
}