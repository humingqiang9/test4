Sub FormatExcelSheet()
    ' Declare variables
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim lastCol As Long
    
    ' Set the active worksheet
    Set ws = ActiveSheet
    
    ' Find the last row and column with data
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    lastCol = ws.Cells(1, ws.Columns.Count).End(xlToLeft).Column
    
    ' Format the header row (assuming first row is header)
    With ws.Range(ws.Cells(1, 1), ws.Cells(1, lastCol))
        .Font.Bold = True
        .Font.Color = RGB(255, 255, 255) ' White font color
        .Interior.Color = RGB(50, 50, 50) ' Dark gray background
        .HorizontalAlignment = xlCenter
    End With
    
    ' Format data rows with alternating colors
    Dim i As Long
    For i = 2 To lastRow
        If i Mod 2 = 0 Then
            ' Even rows - light gray
            ws.Rows(i).Interior.Color = RGB(240, 240, 240)
        Else
            ' Odd rows - white
            ws.Rows(i).Interior.Color = RGB(255, 255, 255)
        End If
    Next i
    
    ' Auto-fit columns
    ws.Columns.AutoFit
    
    ' Add borders to all cells with data
    With ws.Range(ws.Cells(1, 1), ws.Cells(lastRow, lastCol))
        .Borders.LineStyle = xlContinuous
        .Borders.Weight = xlThin
    End With
    
    ' Display message when done
    MsgBox "Sheet formatting complete!", vbInformation
End Sub