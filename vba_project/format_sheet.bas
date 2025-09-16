Sub FormatExcelSheet()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim lastCol As Long
    Dim rng As Range
    
    ' Set the active worksheet
    Set ws = ActiveSheet
    
    ' Find the last row and column with data
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    lastCol = ws.Cells(1, ws.Columns.Count).End(xlToLeft).Column
    
    ' Define the data range
    Set rng = ws.Range(ws.Cells(1, 1), ws.Cells(lastRow, lastCol))
    
    ' Auto-fit columns
    ws.Columns.AutoFit
    
    ' Format header row
    ws.Range(ws.Cells(1, 1), ws.Cells(1, lastCol)).Font.Bold = True
    ws.Range(ws.Cells(1, 1), ws.Cells(1, lastCol)).Interior.Color = RGB(200, 200, 200)
    
    ' Add borders to all cells
    rng.Borders.LineStyle = xlContinuous
    rng.Borders.Weight = xlThin
    
    ' Apply alternating row colors
    Dim i As Long
    For i = 2 To lastRow
        If i Mod 2 = 0 Then
            ws.Range(ws.Cells(i, 1), ws.Cells(i, lastCol)).Interior.Color = RGB(240, 240, 240)
        Else
            ws.Range(ws.Cells(i, 1), ws.Cells(i, lastCol)).Interior.Color = RGB(255, 255, 255)
        End If
    Next i
    
    ' Optional: Freeze the header row
    ws.Range("A2").Select
    ActiveWindow.FreezePanes = True
    
    ' Return to the first cell
    ws.Range("A1").Select
    
    MsgBox "Sheet formatting complete!"
End Sub