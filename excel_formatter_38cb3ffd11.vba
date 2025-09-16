Sub FormatExcelSheet()
    ' Get the active worksheet
    Dim ws As Worksheet
    Set ws = ActiveSheet
    
    ' Format the header row
    With ws.Range("A1:E1")
        .Font.Bold = True
        .Font.Size = 12
        .Interior.Color = RGB(200, 200, 200)
        .Borders.LineStyle = xlContinuous
    End With
    
    ' Auto-fit columns
    ws.Columns("A:E").AutoFit
    
    ' Format data range
    With ws.Range("A2:E100")
        .Borders.LineStyle = xlContinuous
        .Borders.Weight = xlThin
    End With
    
    ' Add a title in cell A1
    ws.Range("A1").Value = "Formatted Data"
    
    ' Center align all cells in the used range
    ws.UsedRange.HorizontalAlignment = xlCenter
    
    MsgBox "Sheet formatting complete!"
End Sub