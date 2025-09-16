Sub FormatExcelSheet()
    ' This macro formats an Excel sheet with various formatting options
    
    Dim ws As Worksheet
    Set ws = ActiveSheet
    
    ' Format the header row
    With ws.Range("A1:E1")
        .Font.Bold = True
        .Font.Size = 12
        .Interior.Color = RGB(79, 129, 189) ' Blue background
        .Font.Color = RGB(255, 255, 255) ' White text
        .HorizontalAlignment = xlCenter
    End With
    
    ' Add borders to all cells in the used range
    ws.UsedRange.Borders.LineStyle = xlContinuous
    ws.UsedRange.Borders.Weight = xlThin
    
    ' Auto-fit columns
    ws.Columns.AutoFit
    
    ' Format data rows with alternating colors
    Dim lastRow As Long
    lastRow = ws.UsedRange.Rows.Count
    
    Dim i As Long
    For i = 2 To lastRow
        If i Mod 2 = 0 Then
            ws.Rows(i).Interior.Color = RGB(219, 229, 241) ' Light blue
        Else
            ws.Rows(i).Interior.Color = RGB(255, 255, 255) ' White
        End If
    Next i
    
    ' Center align all data
    ws.UsedRange.HorizontalAlignment = xlCenter
    
    ' Add a title in cell A1 if it's empty
    If ws.Range("A1").Value = "" Then
        ws.Range("A1").Value = "Formatted Data"
    End If
    
    MsgBox "Sheet formatting complete!"
End Sub