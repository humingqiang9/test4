Sub FormatExcelSheet()
    ' This macro formats an Excel sheet with common formatting options
    
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
    
    ' Format data range
    With ws.Range("A2:E100")
        .Borders.LineStyle = xlContinuous
        .Borders.Weight = xlThin
        .HorizontalAlignment = xlLeft
        .VerticalAlignment = xlCenter
    End With
    
    ' Auto-fit columns
    ws.Columns("A:E").AutoFit
    
    ' Add a title
    ws.Range("A1").EntireRow.Insert
    ws.Range("A1:E1").Merge
    ws.Range("A1").Value = "Formatted Data Report"
    ws.Range("A1").Font.Bold = True
    ws.Range("A1").Font.Size = 16
    ws.Range("A1").HorizontalAlignment = xlCenter
    
    ' Freeze the header row
    ws.Range("A2").Select
    ActiveWindow.FreezePanes = True
    
    ' Add alternating row colors
    Dim i As Long
    For i = 3 To ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
        If i Mod 2 = 0 Then
            ws.Range("A" & i & ":E" & i).Interior.Color = RGB(217, 225, 242) ' Light blue
        Else
            ws.Range("A" & i & ":E" & i).Interior.Color = RGB(255, 255, 255) ' White
        End If
    Next i
    
    MsgBox "Sheet formatting complete!", vbInformation
End Sub