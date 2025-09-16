Sub FormatExcelSheet()
    Dim ws As Worksheet
    Set ws = ActiveSheet
    
    ' Auto-fit columns and rows
    ws.Columns.AutoFit
    ws.Rows.AutoFit
    
    ' Format header row (assuming headers are in row 1)
    With ws.Range("1:1")
        .Font.Bold = True
        .Interior.Color = RGB(200, 200, 200) ' Light gray background
        .Borders.LineStyle = xlContinuous
    End With
    
    ' Format all cells with borders
    ws.Cells.Borders.LineStyle = xlContinuous
    ws.Cells.Borders.Weight = xlThin
    
    ' Center align all cells
    ws.Cells.HorizontalAlignment = xlCenter
    ws.Cells.VerticalAlignment = xlCenter
    
    ' Apply alternating row colors (zebra striping) starting from row 2
    Dim lastRow As Long
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    
    Dim i As Long
    For i = 2 To lastRow
        If i Mod 2 = 0 Then
            ws.Range("A" & i & ":" & ws.Cells(i, ws.Columns.Count).End(xlToLeft).Address).Interior.Color = RGB(240, 240, 240) ' Light gray
        Else
            ws.Range("A" & i & ":" & ws.Cells(i, ws.Columns.Count).End(xlToLeft).Address).Interior.Color = RGB(255, 255, 255) ' White
        End If
    Next i
    
    ' Add a title in cell A1 if it's empty
    If ws.Range("A1").Value = "" Then
        ws.Range("A1").Value = "Formatted Data"
    End If
    
    MsgBox "Sheet formatting complete!"
End Sub