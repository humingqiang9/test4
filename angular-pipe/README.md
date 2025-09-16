# Date Format Pipe for Angular

This Angular pipe allows you to format dates in various formats within your templates.

## Usage

1. Import the pipe in your module:

```typescript
import { DateFormatPipe } from './date-format.pipe';

@NgModule({
  declarations: [DateFormatPipe, /* other components */],
  // ...
})
export class YourModule { }
```

2. Use the pipe in your templates:

```html
<!-- Default short date format -->
<p>{{ someDate | dateFormat }}</p>

<!-- Long date format -->
<p>{{ someDate | dateFormat:'longDate' }}</p>

<!-- Custom format -->
<p>{{ someDate | dateFormat:'MM-dd-yyyy HH:mm' }}</p>
```

## Available Formats

- `shortDate`: MM/dd/yyyy (default)
- `longDate`: MMMM dd, yyyy
- `shortTime`: hh:mm a
- `longTime`: hh:mm:ss a
- `dateTime`: MM/dd/yyyy hh:mm a

You can also pass a custom format string using these placeholders:
- `MM`: Month (01-12)
- `dd`: Day (01-31)
- `yyyy`: Year (4 digits)
- `MMMM`: Full month name
- `hh`: Hours (01-12)
- `HH`: Hours (00-23)
- `mm`: Minutes (00-59)
- `ss`: Seconds (00-59)
- `a`: AM/PM