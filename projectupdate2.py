#Import Library
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import OpenGL.GLUT as glut
print("Imports successful!")


merah1 = 160
hijau1 = 89
biru1 = 201

merah2 = 252
hijau2 = 3
biru2 = 3

merah3 = 160
hijau3 = 89
biru3 = 201

merah4 = 252
hijau4 = 3
biru4 = 3

merah5 = 160
hijau5 = 89
biru5 = 201

merah6 = 160
hijau6 = 89
biru6 = 201

merah7 = 252
hijau7 = 3
biru7 = 3

merah8 = 160
hijau8 = 89
biru8 = 201

merah9 = 160
hijau9 = 89
biru9 = 201

merah10 = 160
hijau10 = 89
biru10 = 201

angle_time1 = 0
angle_time2 = 0
angle_time3 = 0
angle_time4 = 0
angle_time5 = 0
angle_time6 = 0
angle_time7 = 0
angle_time8 = 0
angle_time9 = 0
angle_time10 = 0


#INI MENU START
def Menu():
    #Kotak mulai
    glPushMatrix()
    glBegin(GL_QUADS)
    glColor3ub(235, 137, 52)
    glVertex2f(200, 0) #A
    glVertex2f(600, 0) #B
    glVertex2f(600, 200) #C
    glVertex2f(200, 200) #D
    glEnd()

    #Kotak keluar
    glBegin(GL_QUADS)
    glColor3ub(235, 137, 52)    
    glVertex2f(800, 0) #E
    glVertex2f(1200, 0) #F
    glVertex2f(1200, 200) #G
    glVertex2f(800, 200) #H
    glEnd()

    #Huruf P
    #lengkungan luar
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)
    glVertex2f(220, 180) #J
    glVertex2f(234, 180) #I13
    glVertex2f(246, 178) #L13
    glVertex2f(257, 173) #K13
    glVertex2f(269, 162) #J13
    glVertex2f(276, 150) #M13
    glVertex2f(280, 134) #N13
    glVertex2f(280, 120) #O13
    glVertex2f(275, 106) #P13
    glVertex2f(269, 97) #Q13
    glVertex2f(256, 86) #R13
    glVertex2f(240, 80) #L
    glVertex2f(240, 20) #K
    glVertex2f(220, 20) #I
    glEnd()
    
    #lengkungan dalam
    glBegin(GL_POLYGON)
    glColor3ub(235, 137, 52)
    glVertex2f(240, 160) #N
    glVertex2f(255, 155) #Z13
    glVertex2f(264, 147) #W13
    glVertex2f(268, 138) #V13
    glVertex2f(268, 121) #U13
    glVertex2f(259, 107) #T13
    glVertex2f(247, 100) #S13
    glVertex2f(240, 100) #M
    glEnd()

    #Huruf L
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)
    glVertex2f(300, 20) #P
    glVertex2f(380, 20) #Q
    glVertex2f(380, 40) #R
    glVertex2f(320, 40) #S
    glVertex2f(320, 180) #T
    glVertex2f(300, 180) #O
    glEnd()

    #Huruf A
    #A luar
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)
    glVertex2f(400, 20) #U
    glVertex2f(420, 20) #V
    glVertex2f(430, 40) #A1
    glVertex2f(450, 40) #B1
    glVertex2f(460, 20) #W
    glVertex2f(480, 20) #Z
    glVertex2f(440, 180) #F1
    glEnd() 

    #A dalam
    glBegin(GL_POLYGON)
    glColor3ub(235, 137, 52)  
    glVertex2f(435, 60) #C1
    glVertex2f(445, 60) #D1
    glVertex2f(440, 140) #E1
    glEnd()

    #Huruf Y
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)
    glVertex2f(530, 19) #L1
    glVertex2f(550, 19) #M1
    glVertex2f(549, 79) #N1
    glVertex2f(580, 180) #J1
    glVertex2f(560, 180) #I1
    glVertex2f(540, 120) #K1
    glVertex2f(520, 180) #H1
    glVertex2f(500, 180) #G1
    glEnd()

    #Huruf E
    #atas
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)
    glVertex2f(820, 180) #Q1
    glVertex2f(900, 180) #R1
    glVertex2f(900, 160) #S1
    glVertex2f(840, 160) #T1
    glVertex2f(820, 160) #penambah
    glEnd()

    #Esamping1
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)
    glVertex2f(840, 160) #T1
    glVertex2f(820, 160) #penambah
    glVertex2f(820, 105) #penambah
    glVertex2f(840, 105) #U1
    glEnd()

    #Etengah
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)
    glVertex2f(840, 105) #U1
    glVertex2f(820, 105) #penambah
    glVertex2f(820, 89) #penambah
    glVertex2f(840, 89) #B2
    glVertex2f(899, 89) #C2
    glVertex2f(899, 105) #V1
    glEnd()

    #Esamping2
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)
    glVertex2f(840, 89) #B2
    glVertex2f(820, 89) #penambah
    glVertex2f(820, 20) #P1
    glVertex2f(840, 20)
    glEnd()

    #Ebawah
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(820, 40) #penambah
    glVertex2f(840, 40) #A2
    glVertex2f(900, 40) #Z1
    glVertex2f(900, 20) #W1
    glVertex2f(820, 20) #P1
    glEnd()

    #Huruf X
    #bagian atas
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(940, 100) #N2
    glVertex2f(920, 180) #I2
    glVertex2f(940, 180) #J2
    glVertex2f(960, 120) #K2
    glVertex2f(980, 180) #L2
    glVertex2f(1000, 180) #M2
    glVertex2f(980, 100) #O2
    glEnd()

    #bagian bawah
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(940, 100) #N2
    glVertex2f(920, 20) #D2
    glVertex2f(940, 20) #E2
    glVertex2f(960, 80) #F2
    glVertex2f(980, 20) #G2
    glVertex2f(1000, 20) #H2
    glVertex2f(980, 100) #O2
    glEnd()

    #Huruf I
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(1020, 20) #S2
    glVertex2f(1060, 20) #R2
    glVertex2f(1060, 180) #Q2
    glVertex2f(1020, 180) #P2
    glEnd()
    
    #Huruf T
    #penutup
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)   
    glVertex2f(1080, 180) #T2
    glVertex2f(1180, 180) #U2
    glVertex2f(1180, 160) #V2
    glVertex2f(1080, 160) #Z2
    glEnd()

    #tiang
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(1120, 160) #A2
    glVertex2f(1120, 20) #B3
    glVertex2f(1140, 20) #C3
    glVertex2f(1140, 160) #W2
    glEnd()

    #Huruf M
    #samping kiri
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)     
    glVertex2f(400, 300) #D3
    glVertex2f(400, 500) #E3
    glVertex2f(450, 500) #F3
    glVertex2f(450, 300) #O3
    glEnd()
    
    #miring kiri
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)   
    glVertex2f(450, 500) #F3
    glVertex2f(500, 400) #G3
    glVertex2f(500, 300) #M3
    glVertex2f(450, 400) #N3
    glEnd()

    #miring kanan
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(500, 400) #G3
    glVertex2f(550, 500) #H3
    glVertex2f(550, 400) #L3
    glVertex2f(500, 300) #M3
    glEnd()

    #samping kanan
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)   
    glVertex2f(550, 500) #H3
    glVertex2f(600, 500) #I3
    glVertex2f(600, 300) #J3
    glVertex2f(550, 300) #K3
    glVertex2f(550, 400) #L3
    glEnd()

    #Huruf A1
    #A dalam
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex2f(725, 369) #Z3
    glVertex2f(773, 369) #A4
    glVertex2f(750, 450) #W3
    glEnd()

    #A samping kiri
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)   
    glVertex2f(750, 500) #V3
    glVertex2f(650, 300) #P3
    glVertex2f(700, 300) #Q3
    glVertex2f(725, 349) #R3
    glVertex2f(774, 349) #S3
    glEnd()

    #A samping kanan
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)   
    glVertex2f(774, 349) #S3
    glVertex2f(800, 300) #T3
    glVertex2f(850, 300) #U3
    glVertex2f(750, 500) #V3
    glEnd()

    #A dalam
    glBegin(GL_POLYGON)
    glColor3f(0, 0, 0)
    glVertex2f(725, 369) #Z3
    glVertex2f(773, 369) #A4
    glVertex2f(750, 450) #W3
    glEnd()

    #Huruf T1
    #atas
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(900, 450) #C4
    glVertex2f(1050, 450) #H4
    glVertex2f(1050, 500) #I4
    glVertex2f(900, 500) #B4
    glEnd()

    #tiang
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(950, 450) #D4
    glVertex2f(950, 300) #E4
    glVertex2f(1000, 300) #F4
    glVertex2f(1000, 450) #G4
    glEnd()

    #Huruf C
    #C luar
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)     
    glVertex2f(1200, 450) #M4 
    glVertex2f(1200, 500) #K4
    glVertex2f(1162, 492) #U12
    glVertex2f(1135, 476) #V12
    glVertex2f(1117, 457) #W12
    glVertex2f(1102, 424) #Z12
    glVertex2f(1100, 388) #A13
    glVertex2f(1110, 356) #B13
    glVertex2f(1127, 331) #C13
    glVertex2f(1158, 308) #D13
    glVertex2f(1200, 300) #J4
    glVertex2f(1200, 350) #L4
    glEnd()

    #C dalam
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)
    glVertex2f(1200, 450) #M4
    glVertex2f(1169, 439) #H13
    glVertex2f(1153, 417) #G13
    glVertex2f(1151, 386) #F13
    glVertex2f(1168, 361) #E13
    glVertex2f(1200, 350) #L4
    glEnd()

    #Huruf H
    #samping kiri
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(1250, 500) #N4
    glVertex2f(1250, 300) #O4
    glVertex2f(1300, 300) #P4
    glVertex2f(1300, 500) #A5
    glEnd()

    #H tengah
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(1300, 424) #Z4
    glVertex2f(1300, 373) #Q4
    glVertex2f(1348, 373) #R4
    glVertex2f(1348, 424) #W4
    glEnd()

    #H samping kanan
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(1350, 500) #V4
    glVertex2f(1350, 300) #S4
    glVertex2f(1400, 300) #T4
    glVertex2f(1400, 500) #U4
    glEnd()

    #Huruf C1
    #C luar
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(250, 800) #C5
    glVertex2f(234, 798) #P7
    glVertex2f(214, 793) #E6
    glVertex2f(192, 781) #F6
    glVertex2f(176, 767) #G6
    glVertex2f(161, 746) #H6
    glVertex2f(154, 730) #J6
    glVertex2f(150, 713) #I6
    glVertex2f(150, 696) #K6
    glVertex2f(151, 682) #L6
    glVertex2f(154, 669) #M6
    glVertex2f(167, 643) #O6
    glVertex2f(188, 621) #Q6
    glVertex2f(209, 608) #S6
    glVertex2f(250, 600) #B5
    glEnd()

    #C dalam
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)  
    glVertex2f(250, 750) #E5
    glVertex2f(226, 744) #Z4
    glVertex2f(208, 728) #B7
    glVertex2f(200, 708) #D7
    glVertex2f(203, 682) #F7
    glVertex2f(220, 660) #H7
    glVertex2f(250, 650) #D5
    glEnd()

    # Huruf O
    #O luar
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(400, 800) #G5
    glVertex2f(380, 798) #E8
    glVertex2f(360, 791) #F8
    glVertex2f(345, 783) #G8
    glVertex2f(333, 774) #H8
    glVertex2f(323, 764) #I8
    glVertex2f(312, 749) #J8
    glVertex2f(306, 735) #K8
    glVertex2f(301, 719) #L8
    glVertex2f(300, 704) #M8
    glVertex2f(300, 686) #N8
    glVertex2f(304, 669) #O8
    glVertex2f(311, 653) #P8
    glVertex2f(320, 640) #Q8
    glVertex2f(329, 629) #R8
    glVertex2f(340, 620) #S8
    glVertex2f(353, 611) #T8
    glVertex2f(366, 605) #U8
    glVertex2f(383, 601) #V8
    glVertex2f(400, 600) #F5
    glVertex2f(419, 601) #Q9
    glVertex2f(428, 604) #P9
    glVertex2f(444, 610) #O9
    glVertex2f(456, 617) #N9
    glVertex2f(468, 626) #M9
    glVertex2f(480, 640) #L9
    glVertex2f(487, 651) #K9
    glVertex2f(498, 680) #I9
    glVertex2f(499, 709) #G9
    glVertex2f(495, 729) #F9
    glVertex2f(488, 747) #E9
    glVertex2f(472, 768) #C9
    glVertex2f(448, 787) #A9
    glVertex2f(432, 794) #Z8
    glVertex2f(400, 800) #G5
    glEnd()


    #O dalam
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)  
    glVertex2f(400, 750) #I5
    glVertex2f(370, 740) #K7
    glVertex2f(351, 712) #M7
    glVertex2f(357, 674) #O7
    glVertex2f(381, 653) #R7
    glVertex2f(400, 650) #H5
    glVertex2f(426, 657) #C8
    glVertex2f(442, 673) #A8
    glVertex2f(449, 698) #W7
    glVertex2f(440, 728) #U7
    glVertex2f(417, 746) #S7
    glEnd()

    #Huruf L1
    #tiang
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(550, 800) #J5
    glVertex2f(550, 600) #K5
    glVertex2f(600, 600) #penambah
    glVertex2f(600, 800) #O5
    glEnd()

    #bawah
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(600, 650) #N5
    glVertex2f(600, 600) #penambah
    glVertex2f(700, 600) #L5
    glVertex2f(700, 650) #M5
    glEnd()

    #Huruf O1
    #luar
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)    
    glVertex2f(850, 800) #Q5
    glVertex2f(820, 795) #M10
    glVertex2f(794, 783) #O10
    glVertex2f(768, 758) #Q10
    glVertex2f(754, 730) #S10
    glVertex2f(750, 698) #U10
    glVertex2f(755, 666) #W10
    glVertex2f(772, 636) #A11
    glVertex2f(794, 616) #C11
    glVertex2f(819, 604) #E11
    glVertex2f(850, 600) #P5
    glVertex2f(882, 605) #A12
    glVertex2f(904, 616) #W11
    glVertex2f(923, 631) #U11
    glVertex2f(938, 653) #S11
    glVertex2f(948, 682) #Q11
    glVertex2f(949, 709) #O11
    glVertex2f(937, 748) #M11
    glVertex2f(920, 771) #K11
    glVertex2f(898, 787) #I11
    glVertex2f(868, 798) #G11
    glEnd() 

    #dalam
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)  
    glVertex2f(850, 750) #S5
    glVertex2f(820, 740) #S9
    glVertex2f(802, 714) #U9
    glVertex2f(802, 685) #W9
    glVertex2f(820, 660) #A10
    glVertex2f(863, 651) #C10
    glVertex2f(892, 673) #E10
    glVertex2f(899, 708) #G10
    glVertex2f(885, 735) #I10
    glVertex2f(873, 744) ##J10
    glVertex2f(861, 748) #K10
    glEnd()

    #Huruf R
    #lengkungan luar
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(1000, 800) #V5
    glVertex2f(1014, 809) #C12
    glVertex2f(1033, 816) #D12
    glVertex2f(1053, 817) #E12
    glVertex2f(1069, 815) #F12
    glVertex2f(1083, 810) #G12
    glVertex2f(1100, 800) #H12
    glVertex2f(1116, 784) #J12
    glVertex2f(1125, 767) #K12
    glVertex2f(1130, 746) #L12
    glVertex2f(1130, 725) #M12
    glVertex2f(1125, 707) #N12
    glVertex2f(1114, 688) #O12
    glVertex2f(1101, 674) #B6
    glEnd()

    #bawah
    glBegin(GL_POLYGON)
    glColor3ub(235, 64, 52)  
    glVertex2f(1000, 800) #V5
    glVertex2f(1000, 600) #U5
    glVertex2f(1050, 600) #T5
    glVertex2f(1050, 673) #W5
    glVertex2f(1100, 600) #Z5
    glVertex2f(1150, 600) #A6
    glVertex2f(1101, 674) #B6
    glEnd()

    #lengkungan dalam
    glBegin(GL_POLYGON)
    glColor3ub(0, 0, 0)  
    glVertex2f(1050, 774) #D6
    glVertex2f(1068, 770) #P12
    glVertex2f(1082, 756) #Q12
    glVertex2f(1086, 728) #R12
    glVertex2f(1078, 713) #S12
    glVertex2f(1050, 700) #C6
    glEnd()
    glPopMatrix()


#FUNGSI OBJEK KELINCI
def Kelinci1():
    glPushMatrix()
    glRotated(angle_time1,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah1, hijau1, biru1)
    glBegin(GL_POLYGON)
    
    #Wajah1
    glVertex2f(58, 100) #C
    glVertex2f(68, 111) #D
    glVertex2f(84, 121) #E
    glVertex2f(104, 128) #F
    glVertex2f(117, 129) #G
    glVertex2f(135, 129) #H
    glVertex2f(150, 126) #I
    glVertex2f(162, 121) #J
    glVertex2f(171, 118) #K
    glVertex2f(182, 111) #L
    glVertex2f(191, 101) #M
    glVertex2f(197, 90) #N
    glVertex2f(200, 77) #O
    glVertex2f(198, 65) #P
    glVertex2f(193, 52) #Q
    glVertex2f(183, 41) #R
    glVertex2f(169, 31) #S
    glVertex2f(150, 24) #T
    glVertex2f(132, 21) #U
    glVertex2f(111, 22) #V
    glVertex2f(89, 27) #W
    glVertex2f(71, 37) #Z
    glVertex2f(60, 48) #A_1
    glVertex2f(53, 60) #B_1
    glVertex2f(50, 73) #C_1
    glVertex2f(52, 88) #D_1
    glEnd()

    #Telinga Kiri1
    glBegin(GL_POLYGON)
    glVertex2f(78, 119) #E_1
    glVertex2f(65, 151) #F_1
    glVertex2f(61, 163) #G_1
    glVertex2f(62, 173) #H_1
    glVertex2f(67, 183) #I_1
    glVertex2f(76, 190) #J_1
    glVertex2f(86, 192) #K_1
    glVertex2f(96, 192) #L_1
    glVertex2f(105, 187) #M_1
    glVertex2f(112, 179) #N_1
    glVertex2f(115, 171) #O_1
    glVertex2f(117, 158) #P_1
    glVertex2f(119, 130) #Q_1
    glEnd()

    #Telinga Kanan1
    glBegin(GL_POLYGON)
    glVertex2f(134, 130) #R_1
    glVertex2f(135, 167) #S_1
    glVertex2f(137, 177) #T_1
    glVertex2f(142, 184) #U_1
    glVertex2f(151, 190) #V_1
    glVertex2f(161, 192) #W_1
    glVertex2f(171, 191) #Z_1
    glVertex2f(180, 185) #A_2
    glVertex2f(186, 178) #B_2
    glVertex2f(189, 171) #C_2
    glVertex2f(189, 165) #D_2
    glVertex2f(187, 153) #E_2
    glVertex2f(177, 129) #F_2
    glVertex2f(172, 117) #G_2
    glEnd()
    glPopMatrix()

def Kelinci2():
    glPushMatrix()
    glRotated(angle_time2,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah2, hijau2, biru2)
    glBegin(GL_POLYGON)

    #Wajah2
    glVertex2f(358, 100) #H_2
    glVertex2f(370, 112) #I_2
    glVertex2f(384, 121) #J_2
    glVertex2f(402, 126) #K_2
    glVertex2f(415, 128) #L_2
    glVertex2f(436, 128) #M_2
    glVertex2f(454, 123) #N_2
    glVertex2f(467, 118) #O_2
    glVertex2f(478, 112) #P_2
    glVertex2f(488, 102) #Q_2
    glVertex2f(495, 92) #R_2
    glVertex2f(499, 80) #S_2
    glVertex2f(498, 67) #T_2
    glVertex2f(494, 53) #U_2
    glVertex2f(485, 43) #V_2
    glVertex2f(472, 32) #W_2
    glVertex2f(455, 24) #Z_2
    glVertex2f(435, 20) #A_3
    glVertex2f(412, 20) #B_3
    glVertex2f(392, 25) #C_3
    glVertex2f(374, 33) #D_3
    glVertex2f(360, 45) #E_3
    glVertex2f(352, 58) #F_3
    glVertex2f(349, 72) #G_3
    glVertex2f(351, 87) #H_3
    glEnd()

    #Telinga Kiri2
    glBegin(GL_POLYGON)
    glVertex2f(375, 115) #I_3
    glVertex2f(363, 152) #J_3
    glVertex2f(360, 163) #K_3
    glVertex2f(363, 176) #L_3
    glVertex2f(371, 186) #M_3
    glVertex2f(380, 190) #N_3
    glVertex2f(391, 191) #O_3
    glVertex2f(400, 188) #P_3
    glVertex2f(407, 184) #Q_3
    glVertex2f(412, 177) #R_3
    glVertex2f(415, 170) #S_3
    glVertex2f(416, 158) #T_3
    glVertex2f(415, 125) #U_3
    glEnd()

    #Telinga Kanan2
    glBegin(GL_POLYGON)
    glVertex2f(432, 125) #V_3
    glVertex2f(434, 163) #W_3
    glVertex2f(436, 175) #Z_3
    glVertex2f(443, 184) #A_4
    glVertex2f(453, 190) #B_4
    glVertex2f(464, 191) #C_4
    glVertex2f(473, 188) #D_4
    glVertex2f(479, 185) #E_4
    glVertex2f(484, 179) #F_4
    glVertex2f(488, 171) #G_4
    glVertex2f(489, 164) #H_4
    glVertex2f(487, 153) #I_4
    glVertex2f(480, 135) #J_4
    glVertex2f(471, 116) #K_4
    glEnd()
    glPopMatrix()

def Kelinci3():
    glPushMatrix()
    glRotated(angle_time3,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah3, hijau3, biru3)
    glBegin(GL_POLYGON)

    #Wajah3
    glVertex2f(58, 400) #L_4
    glVertex2f(69, 411) #M_4
    glVertex2f(85, 421) #N_4
    glVertex2f(101, 426) #O_4
    glVertex2f(115, 428) #P_4
    glVertex2f(135, 428) #Q_4
    glVertex2f(153, 423) #R_4
    glVertex2f(167, 418) #S_4
    glVertex2f(176, 413) #T_4
    glVertex2f(189, 401) #U_4
    glVertex2f(196, 389) #V_4
    glVertex2f(199, 377) #W_4
    glVertex2f(198, 365) #Z_4
    glVertex2f(194, 355) #A_5
    glVertex2f(188, 346) #B_5
    glVertex2f(178, 336) #C_5
    glVertex2f(162, 326) #D_5
    glVertex2f(142, 321) #E_5
    glVertex2f(122, 319) #F_5
    glVertex2f(101, 322) #G_5
    glVertex2f(85, 327) #H_5
    glVertex2f(71, 336) #I_5
    glVertex2f(60, 346) #J_5
    glVertex2f(53, 357) #K_5
    glVertex2f(50, 367) #L_5
    glVertex2f(50, 380) #M_5
    glVertex2f(53, 392) #N_5
    glEnd()

    #Telinga Kiri3
    glBegin(GL_POLYGON)
    glVertex2f(75, 415) #O_5
    glVertex2f(62, 455) #P_5
    glVertex2f(60, 464) #Q_5
    glVertex2f(62, 474) #R_5
    glVertex2f(68, 484) #S_5
    glVertex2f(78, 489) #T_5
    glVertex2f(87, 491) #U_5
    glVertex2f(97, 490) #V_5
    glVertex2f(103, 486) #W_5
    glVertex2f(110, 480) #Z_5
    glVertex2f(113, 473) #A_6
    glVertex2f(116, 462) #B_6
    glVertex2f(117, 446) #C_6
    glVertex2f(115, 428) #D_6
    glEnd()

    #Telinga Kanan3
    glBegin(GL_POLYGON)
    glVertex2f(131, 428) #E_6
    glVertex2f(133, 464) #F_6
    glVertex2f(137, 476) #G_6
    glVertex2f(144, 484) #H_6
    glVertex2f(152, 489) #I_6
    glVertex2f(161, 491) #J_6
    glVertex2f(170, 490) #K_6
    glVertex2f(178, 485) #L_6
    glVertex2f(184, 478) #M_6
    glVertex2f(188, 470) #N_6
    glVertex2f(189, 462) #O_6
    glVertex2f(186, 452) #P_6
    glVertex2f(177, 430) #Q_6
    glVertex2f(171, 416) #R_6
    glEnd()
    glPopMatrix()

def Kelinci4():
    glPushMatrix()
    glRotated(angle_time4,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah4, hijau4, biru4)
    glBegin(GL_POLYGON)

    #Wajah4
    glVertex2f(358, 400) #S_6
    glVertex2f(371, 413) #T_6
    glVertex2f(384, 420) #U_6
    glVertex2f(398, 426) #V_6
    glVertex2f(415, 428) #W_6
    glVertex2f(435, 428) #Z_6
    glVertex2f(451, 424) #A_7
    glVertex2f(467, 418) #B_7
    glVertex2f(475, 414) #C_7
    glVertex2f(483, 407) #D_7
    glVertex2f(490, 399) #E_7
    glVertex2f(496, 391) #F_7
    glVertex2f(498, 381) #G_7
    glVertex2f(499, 373) #H_7
    glVertex2f(498, 364) #I_7
    glVertex2f(495, 355) #J_7
    glVertex2f(488, 345) #K_7
    glVertex2f(476, 335) #L_7
    glVertex2f(462, 327) #M_7
    glVertex2f(449, 323) #N_7
    glVertex2f(434, 320) #O_7
    glVertex2f(419, 320) #P_7
    glVertex2f(400, 322) #Q_7
    glVertex2f(384, 328) #R_7
    glVertex2f(368, 338) #S_7
    glVertex2f(358, 349) #T_7
    glVertex2f(352, 359) #U_7
    glVertex2f(350, 370) #V_7
    glVertex2f(350, 380) #W_7
    glVertex2f(353, 392) #Z_7
    glEnd()

    #Telinga Kiri4
    glBegin(GL_POLYGON)
    glVertex2f(378, 417) #A_8
    glVertex2f(363, 450) #B_8
    glVertex2f(361, 460) #C_8
    glVertex2f(361, 468) #D_8
    glVertex2f(364, 476) #E_8
    glVertex2f(369, 484) #F_8
    glVertex2f(376, 488) #G_8
    glVertex2f(385, 491) #H_8
    glVertex2f(394, 491) #I_8
    glVertex2f(402, 487) #J_8
    glVertex2f(409, 481) #K_8
    glVertex2f(413, 474) #L_8
    glVertex2f(416, 465) #M_8
    glVertex2f(417, 445) #N_8
    glVertex2f(418, 428) #O_8
    glEnd()

    #Telinga Kanan4
    glBegin(GL_POLYGON)
    glVertex2f(432, 428) #P_8
    glVertex2f(433, 461) #Q_8
    glVertex2f(437, 475) #R_8
    glVertex2f(442, 484) #S_8
    glVertex2f(452, 489) #T_8
    glVertex2f(463, 491) #U_8
    glVertex2f(473, 488) #V_8
    glVertex2f(481, 483) #W_8
    glVertex2f(486, 476) #Z_8
    glVertex2f(488, 468) #A_9
    glVertex2f(488, 460) #B_9
    glVertex2f(485, 449) #C_9
    glVertex2f(477, 428) #D_9
    glVertex2f(471, 416) #E_9
    glEnd()
    glPopMatrix()

def Kelinci5():
    glPushMatrix()
    glRotated(angle_time5,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah5, hijau5, biru5)
    glBegin(GL_POLYGON)

    #Wajah5
    glVertex2f(660, 400) #R_11
    glVertex2f(671, 412) #S_11
    glVertex2f(685, 419) #T_11
    glVertex2f(701, 425) #U_11
    glVertex2f(714, 427) #V_11
    glVertex2f(736, 427) #W_11
    glVertex2f(754, 422) #Z_11
    glVertex2f(768, 417) #A_12
    glVertex2f(779, 411) #B_12
    glVertex2f(791, 399) #C_12
    glVertex2f(798, 386) #D_12
    glVertex2f(800, 374) #E_12
    glVertex2f(798, 363) #F_12
    glVertex2f(794, 351) #G_12
    glVertex2f(781, 337) #H_12
    glVertex2f(764, 326) #I_12
    glVertex2f(745, 321) #J_12
    glVertex2f(727, 319) #K_12
    glVertex2f(711, 320) #L_12
    glVertex2f(688, 326) #M_12
    glVertex2f(674, 334) #N_12
    glVertex2f(663, 343) #O_12
    glVertex2f(656, 353) #P_12
    glVertex2f(651, 365) #Q_12
    glVertex2f(650, 379) #R_12
    glVertex2f(654, 392) #S_12
    glEnd()

    #Telinga Kiri5
    glBegin(GL_POLYGON)
    glVertex2f(679, 416) #T_12
    glVertex2f(666, 446) #U_12
    glVertex2f(662, 460) #V_12
    glVertex2f(662, 470) #W_12
    glVertex2f(666, 479) #Z_12
    glVertex2f(673, 485) #A_13
    glVertex2f(681, 489) #B_13
    glVertex2f(690, 491) #C_13
    glVertex2f(699, 489) #D_13
    glVertex2f(706, 485) #E_13
    glVertex2f(711, 479) #F_13
    glVertex2f(715, 472) #G_13
    glVertex2f(716, 464) #H_13
    glVertex2f(717, 455) #I_13
    glVertex2f(719, 428) #J_13
    glEnd()

    #Telinga Kanan5
    glBegin(GL_POLYGON)
    glVertex2f(732, 428) #K_13
    glVertex2f(734, 462) #L_13
    glVertex2f(737, 474) #M_13
    glVertex2f(743, 483) #N_13
    glVertex2f(753, 489) #O_13
    glVertex2f(762, 490) #P_13
    glVertex2f(770, 490) #Q_13
    glVertex2f(777, 486) #R_13
    glVertex2f(783, 481) #S_13
    glVertex2f(788, 473) #T_13
    glVertex2f(789, 465) #U_13
    glVertex2f(789, 457) #V_13
    glVertex2f(783, 442) #W_13
    glVertex2f(772, 415) #Z_13
    glEnd()
    glPopMatrix()

def Kelinci6():
    glPushMatrix()
    glRotated(angle_time6,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah6, hijau6, biru6)
    glBegin(GL_POLYGON)

    #Wajah6
    glVertex2f(660, 100) #F_9
    glVertex2f(671, 111) #G_9
    glVertex2f(684, 118) #H_9
    glVertex2f(698, 123) #I_9
    glVertex2f(713, 126) #J_9
    glVertex2f(734, 126) #K_9
    glVertex2f(749, 122) #L_9
    glVertex2f(767, 116) #M_9
    glVertex2f(777, 110) #N_9
    glVertex2f(788, 100) #O_9
    glVertex2f(794, 92) #P_9
    glVertex2f(797, 82) #Q_9
    glVertex2f(799, 73) #R_9
    glVertex2f(798, 61) #S_9
    glVertex2f(793, 51) #T_9
    glVertex2f(786, 41) #U_9
    glVertex2f(774, 32) #V_9
    glVertex2f(760, 24) #W_9
    glVertex2f(742, 19) #Z_9
    glVertex2f(721, 18) #A_10
    glVertex2f(700, 20) #B_10
    glVertex2f(681, 28) #C_10
    glVertex2f(667, 36) #D_10
    glVertex2f(657, 47) #E_10
    glVertex2f(652, 58) #F_10
    glVertex2f(649, 69) #G_10
    glVertex2f(650, 82) #H_10
    glVertex2f(654, 92) #I_10
    glEnd()

    #Telinga Kiri6
    glBegin(GL_POLYGON)
    glVertex2f(678, 115) #J_10
    glVertex2f(667, 139) #K_10
    glVertex2f(661, 157) #L_10
    glVertex2f(661, 165) #M_10
    glVertex2f(663, 174) #N_10
    glVertex2f(669, 182) #O_10
    glVertex2f(678, 188) #P_10
    glVertex2f(687, 189) #Q_10
    glVertex2f(697, 188) #R_10
    glVertex2f(705, 183) #S_10
    glVertex2f(711, 177) #T_10
    glVertex2f(714, 169) #U_10
    glVertex2f(716, 155) #V_10
    glVertex2f(717, 137) #W_10
    glVertex2f(718, 126) #Z_10
    glEnd()

    #Telinga Kanan6
    glBegin(GL_POLYGON)
    glVertex2f(731, 126) #A_11
    glVertex2f(733, 161) #B_11
    glVertex2f(736, 172) #C_11
    glVertex2f(740, 179) #D_11
    glVertex2f(746, 185) #E_11
    glVertex2f(754, 188) #F_11
    glVertex2f(761, 189) #G_11
    glVertex2f(769, 188) #H_11
    glVertex2f(775, 185) #I_11
    glVertex2f(781, 180) #J_11
    glVertex2f(785, 175) #K_11
    glVertex2f(787, 169) #L_11
    glVertex2f(788, 163) #M_11
    glVertex2f(787, 155) #N_11
    glVertex2f(783, 142) #O_11
    glVertex2f(776, 124) #P_11
    glVertex2f(771, 114) #Q_11
    glEnd()
    glPopMatrix()
    
def Kelinci7():
    glPushMatrix()
    glRotated(angle_time7,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah7, hijau7, biru7)
    glBegin(GL_POLYGON)

    #Wajah7
    glVertex2f(959, 400) #I_18
    glVertex2f(969, 410) #J_18
    glVertex2f(981, 418) #K_18
    glVertex2f(1000, 426) #L_18
    glVertex2f(1016, 428) #M_18
    glVertex2f(1035, 428) #N_18
    glVertex2f(1051, 424) #O_18
    glVertex2f(1068, 418) #P_18
    glVertex2f(1078, 412) #Q_18
    glVertex2f(1088, 402) #R_18
    glVertex2f(1096, 391) #S_18
    glVertex2f(1100, 380) #T_18
    glVertex2f(1099, 365) #U_18
    glVertex2f(1094, 352) #V_18
    glVertex2f(1085, 341) #W_18
    glVertex2f(1071, 331) #Z_18
    glVertex2f(1052, 323) #A_19
    glVertex2f(1031, 320) #B_19
    glVertex2f(1008, 321) #C_19
    glVertex2f(990, 326) #D_19
    glVertex2f(973, 335) #E_19
    glVertex2f(958, 349) #F_19
    glVertex2f(952, 362) #G_19
    glVertex2f(950, 374) #H_19
    glVertex2f(952, 388) #I_19
    glEnd()

    #Telinga Kiri7
    glBegin(GL_POLYGON)
    glVertex2f(978, 418) #J_19
    glVertex2f(965, 448) #K_19
    glVertex2f(962, 460) #L_19
    glVertex2f(962, 469) #M_19
    glVertex2f(965, 477) #N_19
    glVertex2f(972, 485) #O_19
    glVertex2f(980, 490) #P_19
    glVertex2f(989, 491) #Q_19
    glVertex2f(998, 490) #R_19
    glVertex2f(1005, 486) #S_19
    glVertex2f(1011, 479) #T_19
    glVertex2f(1015, 471) #U_19
    glVertex2f(1016, 461) #V_19
    glVertex2f(1018, 443) #W_19
    glVertex2f(1019, 428) #Z_19
    glEnd()

    #Telinga Kanan7
    glBegin(GL_POLYGON)
    glVertex2f(1032, 428) #A_20
    glVertex2f(1035, 466) #B_20
    glVertex2f(1038, 477) #C_20
    glVertex2f(1044, 484) #D_20
    glVertex2f(1052, 489) #E_20
    glVertex2f(1062, 491) #F_20
    glVertex2f(1071, 489) #G_20
    glVertex2f(1079, 485) #H_20
    glVertex2f(1084, 479) #I_20
    glVertex2f(1088, 472) #J_20
    glVertex2f(1089, 463) #K_20
    glVertex2f(1088, 454) #L_20
    glVertex2f(1080, 433) #M_20
    glVertex2f(1072, 416) #N_20
    glEnd()
    glPopMatrix()

def Kelinci8():
    glPushMatrix()
    glRotated(angle_time8,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah8, hijau8, biru8) 
    glBegin(GL_POLYGON)

    #Wajah8
    glVertex2f(960, 100) #A_14
    glVertex2f(971, 111) #B_14
    glVertex2f(983, 119) #C_14
    glVertex2f(996, 124) #D_14
    glVertex2f(1014, 128) #E_14
    glVertex2f(1036, 127) #F_14
    glVertex2f(1052, 123) #G_14
    glVertex2f(1067, 118) #H_14
    glVertex2f(1078, 111) #I_14
    glVertex2f(1089, 102) #J_14
    glVertex2f(1096, 90) #K_14
    glVertex2f(1100, 77) #L_14
    glVertex2f(1099, 64) #M_14
    glVertex2f(1092, 50) #N_14
    glVertex2f(1080, 37) #O_14
    glVertex2f(1063, 26) #P_14
    glVertex2f(1044, 21) #Q_14
    glVertex2f(1025, 19) #R_14
    glVertex2f(1003, 21) #S_14
    glVertex2f(984, 28) #T_14
    glVertex2f(967, 39) #U_14
    glVertex2f(957, 51) #V_14
    glVertex2f(950, 66) #W_14
    glVertex2f(951, 83) #Z_14
    glEnd()

    #Telinga Kiri8
    glBegin(GL_POLYGON)
    glVertex2f(979, 116) #A_15
    glVertex2f(966, 146) #B_15
    glVertex2f(962, 159) #C_15
    glVertex2f(961, 168) #D_15
    glVertex2f(966, 179) #E_15
    glVertex2f(974, 186) #F_15
    glVertex2f(982, 190) #G_15
    glVertex2f(991, 191) #H_15
    glVertex2f(1002, 187) #I_15
    glVertex2f(1009, 182) #J_15
    glVertex2f(1014, 172) #K_15
    glVertex2f(1016, 163) #L_15
    glVertex2f(1017, 152) #M_15
    glVertex2f(1019, 128) #N_15
    glEnd()

    #Telinga Kanan8
    glBegin(GL_POLYGON)
    glVertex2f(1032, 128) #O_15
    glVertex2f(1035, 163) #P_15
    glVertex2f(1037, 174) #Q_15
    glVertex2f(1041, 181) #R_15
    glVertex2f(1049, 187) #S_15
    glVertex2f(1058, 190) #T_15
    glVertex2f(1066, 190) #U_15
    glVertex2f(1072, 188) #V_15
    glVertex2f(1079, 184) #W_15
    glVertex2f(1085, 178) #Z_15
    glVertex2f(1088, 170) #A_16
    glVertex2f(1089, 163) #B_16
    glVertex2f(1088, 154) #C_16
    glVertex2f(1082, 138) #D_16
    glVertex2f(1072, 115) #E_16
    glEnd()
    glPopMatrix()

def Kelinci9():
    glPushMatrix()
    glRotated(angle_time9,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah9, hijau9, biru9)
    glBegin(GL_POLYGON)

    #Wajah9
    glVertex2f(1258, 400) #O_20
    glVertex2f(1268, 410) #P_20
    glVertex2f(1281, 419) #Q_20
    glVertex2f(1296, 425) #R_20
    glVertex2f(1314, 428) #S_20
    glVertex2f(1336, 428) #T_20
    glVertex2f(1353, 424) #U_20
    glVertex2f(1368, 417) #V_20
    glVertex2f(1377, 412) #W_20
    glVertex2f(1387, 403) #Z_20
    glVertex2f(1394, 393) #A_21
    glVertex2f(1399, 381) #B_21
    glVertex2f(1400, 370) #C_21
    glVertex2f(1396, 356) #D_21
    glVertex2f(1388, 345) #E_21
    glVertex2f(1377, 335) #F_21
    glVertex2f(1362, 327) #G_21
    glVertex2f(1343, 321) #H_21
    glVertex2f(1326, 320) #I_21
    glVertex2f(1308, 321) #J_21
    glVertex2f(1289, 326) #K_21
    glVertex2f(1273, 335) #L_21
    glVertex2f(1261, 345) #M_21
    glVertex2f(1253, 358) #N_21
    glVertex2f(1250, 373) #O_21
    glVertex2f(1252, 387) #P_21
    glEnd()

    #Telinga Kiri9
    glBegin(GL_POLYGON)
    glVertex2f(1278, 416) #Q_21
    glVertex2f(1264, 450) #R_21
    glVertex2f(1262, 459) #S_21
    glVertex2f(1261, 468) #T_21
    glVertex2f(1265, 478) #U_21
    glVertex2f(1272, 486) #V_21
    glVertex2f(1280, 490) #W_21
    glVertex2f(1289, 491) #Z_21
    glVertex2f(1298, 489) #A_22
    glVertex2f(1304, 486) #B_22
    glVertex2f(1311, 480) #C_22
    glVertex2f(1315, 470) #D_22
    glVertex2f(1316, 456) #E_22
    glVertex2f(1318, 428) #F_22
    glEnd()

    #Telinga Kanan9
    glBegin(GL_POLYGON)
    glVertex2f(1332, 428) #G_22
    glVertex2f(1334, 465) #H_22
    glVertex2f(1337, 476) #I_22
    glVertex2f(1343, 484) #J_22
    glVertex2f(1354, 490) #K_22
    glVertex2f(1363, 491) #L_22
    glVertex2f(1372, 489) #M_22
    glVertex2f(1378, 485) #N_22
    glVertex2f(1385, 478) #O_22
    glVertex2f(1388, 472) #P_22
    glVertex2f(1389, 464) #Q_22
    glVertex2f(1388, 457) #R_22
    glVertex2f(1384, 444) #S_22
    glVertex2f(1371, 416) #T_22
    glEnd()
    glPopMatrix()

def Kelinci10():
    glPushMatrix()
    glRotated(angle_time10,0,0,1)
    glScaled(2, 2, 0)
    glColor3ub(merah10, hijau10, biru10)
    glBegin(GL_POLYGON)

    #Wajah10
    glVertex2f(1258, 100) #F_16
    glVertex2f(1271, 112) #G_16
    glVertex2f(1283, 119) #H_16
    glVertex2f(1301, 125) #I_16
    glVertex2f(1313, 127) #J_16
    glVertex2f(1335, 127) #K_16
    glVertex2f(1352, 123) #L_16
    glVertex2f(1367, 118) #M_16
    glVertex2f(1377, 112) #N_16
    glVertex2f(1388, 102) #O_16
    glVertex2f(1396, 90) #P_16
    glVertex2f(1399, 77) #Q_16
    glVertex2f(1398, 65) #R_16
    glVertex2f(1393, 52) #S_16
    glVertex2f(1385, 42) #T_16
    glVertex2f(1368, 29) #U_16
    glVertex2f(1350, 23) #V_16
    glVertex2f(1329, 19) #W_16
    glVertex2f(1304, 21) #Z_16
    glVertex2f(1283, 28) #A_17
    glVertex2f(1266, 39) #B_17
    glVertex2f(1255, 52) #C_17
    glVertex2f(1250, 70) #D_17
    glVertex2f(1251, 86) #E_17
    glEnd()

    #Telinga Kiri10
    glBegin(GL_POLYGON)
    glVertex2f(1278, 116) #F_17
    glVertex2f(1264, 150) #G_17
    glVertex2f(1261, 162) #H_17
    glVertex2f(1263, 174) #I_17
    glVertex2f(1269, 183) #J_17
    glVertex2f(1277, 188) #K_17
    glVertex2f(1286, 191) #L_17
    glVertex2f(1296, 189) #M_17
    glVertex2f(1304, 186) #N_17
    glVertex2f(1311, 178) #O_17
    glVertex2f(1314, 170) #P_17
    glVertex2f(1316, 157) #Q_17
    glVertex2f(1318, 127) #R_17
    glEnd()

    #Telinga Kanan10
    glBegin(GL_POLYGON)
    glVertex2f(1332, 127) #S_17
    glVertex2f(1334, 163) #T_17
    glVertex2f(1336, 173) #U_17
    glVertex2f(1341, 182) #V_17
    glVertex2f(1350, 188) #W_17
    glVertex2f(1360, 190) #Z_17
    glVertex2f(1368, 190) #A_18
    glVertex2f(1376, 186) #B_18
    glVertex2f(1383, 180) #C_18
    glVertex2f(1388, 171) #D_18
    glVertex2f(1389, 162) #E_18
    glVertex2f(1386, 152) #F_18
    glVertex2f(1381, 137) #G_18
    glVertex2f(1371, 115) #H_18
    glEnd()
    glPopMatrix()


#FUNGSI UBAH WARNA KELINCI
def iniHandleMouse(button, state, x, y):
    global merah1, hijau1, biru1, game_over
    global merah2, hijau2, biru2, game_over
    global merah3, hijau3, biru3, game_over
    global merah4, hijau4, biru4, game_over
    global merah5, hijau5, biru5, game_over
    global merah6, hijau6, biru6, game_over
    global merah7, hijau7, biru7, game_over
    global merah8, hijau8, biru8, game_over
    global merah9, hijau9, biru9, game_over
    global merah10, hijau10, biru10, game_over
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah1 == 160 and hijau1 == 89 and biru1 == 201 and 42<x<95 and 325<y<410 :
            merah1 = 66
            hijau1 = 135
            biru1 = 245
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if (merah1 == 66 and hijau1 == 135 and biru1 == 245) or (merah1 == 160 and hijau1 == 89 and biru1 == 201) and 42<x<95 and 325<y<410 :
            merah1 = 252
            hijau1 = 3
            biru1 = 3
            game_over = False
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah2 == 252 and hijau2 == 3 and biru2 == 3 and 149<x<202 and 330<y<414 :
            merah2 = 66
            hijau2 = 135
            biru2 = 245
            game_over = True
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if merah2 == 252 and hijau2 == 3 and biru2 == 3 and 149<x<202 and 330<y<414 :
            merah2 = 160
            hijau2 = 89
            biru2 = 201
            game_over = True
        print("Klik Kiri ditekan ", "(", x, ",", y, ")")

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah3 == 160 and hijau3 == 89 and biru3 == 201 and 41<x<97 and 178<y<263 :
            merah3 = 66
            hijau3 = 135
            biru3 = 245
            game_over = True
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if merah3 == 160 and hijau3 == 89 and biru3 == 201 and 41<x<97 and 178<y<263 :
            merah3 = 252
            hijau3 = 3
            biru3 = 3
            game_over = False
        print("Klik Kiri ditekan ", "(", x, ",", y, ")")

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah4 == 252 and hijau4 == 3 and biru4 == 3 and 151<x<203 and 170<y<256 :
            merah4 = 66
            hijau4 = 135
            biru4 = 245
            game_over = True
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if merah4 == 252 and hijau4 == 3 and biru4 == 3 and 151<x<203 and 170<y<256 :
            merah4 = 160
            hijau4 = 89
            biru4 = 201
            game_over = True
        print("Klik Kiri ditekan ", "(", x, ",", y, ")")

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah5 == 160 and hijau5 == 89 and biru5 == 201 and 255<x<308 and 181<y<263 :
            merah5 = 66
            hijau5 = 135
            biru5 = 245
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if (merah5 == 66 and hijau5 == 135 and biru5 == 245) or (merah5 == 160 and hijau5 == 89 and biru5 == 201) and 255<x<308 and 181<y<263 :
            merah5 = 252
            hijau5 = 3
            biru5 = 3
            game_over = False
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah6 == 160 and hijau6 == 89 and biru6 == 201 and 256<x<310 and 329<y<413 :
            merah6 = 66
            hijau6 = 135
            biru6 = 245
            game_over = True
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if merah6 == 160 and hijau6 == 89 and biru6 == 201 and 256<x<310 and 329<y<413 :
            merah6 = 252
            hijau6 = 3
            biru6 = 3
            game_over = False
        print("Klik Kiri ditekan ", "(", x, ",", y, ")")

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah7 == 252 and hijau7 == 3 and biru7 == 3 and 362<x<418 and 178<y<262 :
            merah7 = 66
            hijau7 = 135
            biru7 = 245
            game_over = True
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if merah7 == 252 and hijau7 == 3 and biru7 == 3 and 362<x<418 and 178<y<262 :
            merah7 = 160
            hijau7 = 89
            biru7 = 201
            game_over = True
        print("Klik Kiri ditekan ", "(", x, ",", y, ")")

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah8 == 160 and hijau8 == 89 and biru8 == 201 and 365<x<416 and 329<y<414 :
            merah8 = 66
            hijau8 = 135
            biru8 = 245
            game_over = True
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if merah8 == 160 and hijau8 == 89 and biru8 == 201 and 365<x<416 and 329<y<414 :
            merah8 = 252
            hijau8 = 3
            biru8 = 3
            game_over = False
        print("Klik Kiri ditekan ", "(", x, ",", y, ")")

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah9 == 160 and hijau9 == 89 and biru9 == 201 and 472<x<524 and 150<y<236 :
            merah9 = 66
            hijau9 = 135
            biru9 = 245
            game_over = True
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if merah9 == 160 and hijau9 == 89 and biru9 == 201 and 472<x<524 and 150<y<236 :
            merah9 = 252
            hijau9 = 3
            biru9 = 3
            game_over = False
        print("Klik Kiri ditekan ", "(", x, ",", y, ")")

    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        if merah10 == 160 and hijau10 == 89 and biru10 == 201 and 471<x<522 and 330<y<414 :
            merah10 = 66
            hijau10 = 135
            biru10 = 245
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if (merah10 == 66 and hijau10 == 135 and biru10 == 245) or (merah10 == 160 and hijau10 == 89 and biru10 == 201) and 471<x<522 and 330<y<414 :
            merah10 = 252
            hijau10 = 3
            biru10 = 3
            game_over = False
        print("Klik Kanan ditekan ", "(", x, ",", y, ")")


#FUNGSI GERAK KELINCI
def timer1(value):
    global angle_time1
    if angle_time1 == 0:
        angle_time1 += 2
    else :
        angle_time1 -= 2
    glutTimerFunc(200, timer1, 0)

def timer2(value):
    global angle_time2
    if angle_time2 == 0:
        angle_time2 += 2
    else :
        angle_time2 -= 2
    glutTimerFunc(210, timer2, 0)

def timer3(value):
    global angle_time3
    if angle_time3 == 0:
        angle_time3 += 2
    else :
        angle_time3 -= 2
    glutTimerFunc(220, timer3, 0)

def timer4(value):
    global angle_time4
    if angle_time4 == 0:
        angle_time4 += 2
    else :
        angle_time4 -= 2
    glutTimerFunc(200, timer4, 0)

def timer5(value):
    global angle_time5
    if angle_time5 == 0:
        angle_time5 += 2
    else :
        angle_time5 -= 2
    glutTimerFunc(210, timer5, 0)

def timer6(value):
    global angle_time6
    if angle_time6 == 0:
        angle_time6 += 2
    else :
        angle_time6 -= 2
    glutTimerFunc(220, timer6, 0)

def timer7(value):
    global angle_time7
    if angle_time7 == 0:
        angle_time7 += 2
    else :
        angle_time7 -= 2
    glutTimerFunc(200, timer7, 0)

def timer8(value):
    global angle_time8
    if angle_time8 == 0:
        angle_time8 += 2
    else :
        angle_time8 -= 2
    glutTimerFunc(210, timer8, 0)

def timer9(value):
    global angle_time9
    if angle_time9 == 0:
        angle_time9 += 2
    else :
        angle_time9 -= 2
    glutTimerFunc(220, timer9, 0)

def timer10(value):
    global angle_time10
    if angle_time10 == 0:
        angle_time10 += 2
    else :
        angle_time10 -= 2
    glutTimerFunc(200, timer10, 0)

#TEXT WIN DAN GAME OVER
game_over = False
def bg_text(x,y):
    glColor3ub(237, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(300+x,100+y)
    glVertex2f(1000+x,100+y)
    glVertex2f(1000+x,350+y)
    glVertex2f(300+x,350+y)
    glEnd()
def drawText(ch,xpos,ypos,r,b,g):
    glPushMatrix()
    color = (r, b, g)
    font_style = glut.GLUT_BITMAP_HELVETICA_18
    glColor3ub(color[0],color[1],color[2])
    line=0
    glRasterPos2f (xpos, ypos)
    for i in ch:
       if  i=='\n':
          line=line+1
          glRasterPos2f (xpos, ypos*line)
       else:
          glutBitmapCharacter(font_style, ord(i))  
    glPopMatrix()  

#FUNGSI GARIS BACKGROUND
def Garis():
    # glColor3f(1.0, 1.0, 1.)
    # glBegin(GL_LINE_LOOP)
    # glVertex2f(2, 0.100)
    # glVertex2f(2, 1100)
    # glEnd()

    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(560, 0.100)
    glVertex2f(560, 1100)
    glEnd()

    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1160, 0.1000)
    glVertex2f(1160, 1100)
    glEnd()

    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(1750, 0.1000)
    glVertex2f(1750, 1100)
    glEnd()

    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(2300, 0.1000)
    glVertex2f(2300, 1100)
    glEnd()

    # glColor3f(1.0, 1.0, 1.)
    # glBegin(GL_LINE_LOOP)
    # glVertex2f(2800.2, 0.1000)
    # glVertex2f(2800.2, 1100)
    # glEnd()

    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0, 0.1000)
    glVertex2f(2800, 0.1000)
    glEnd()

    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0, 1100)
    glVertex2f(2800, 1100)
    glEnd()

    glColor3f(1.0, 1.0, 1.)
    glBegin(GL_LINE_LOOP)
    glVertex2f(0, 550)
    glVertex2f(2800, 550)
    glEnd()


#Fungsi Iterasi untuk looping keseluruhan program agar workspace tidak hilang tiba-tiba
def iterate():
    glViewport(25, 75, 500, 500) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 2800, 0.0, 2000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #untuk membersihkan layar
    glLoadIdentity() #untuk mereset semua posisi grafik stsu bentuk
    iterate() #fungsi looping
    if merah1 == merah2 == merah3 == merah4 == merah5 == merah6 == merah7 == merah8 == merah9 == merah10 == 252 and game_over == False:
        bg_text(900, 600)
        drawText("YOU WIN!!!",1255,805,50,200,50)
    elif game_over == True:
        bg_text(900, 600)
        drawText("GAME OVER",1245,795,50,200,50)
    else:
        # Menu()
        Kelinci1()
        Kelinci2()
        Kelinci3()
        Kelinci4()
        Kelinci5()
        Kelinci6()
        Kelinci7()
        Kelinci8()
        Kelinci9()
        Kelinci10()
        Garis()

    glutSwapBuffers() #untuk membersihkan layar


#Inisialisasi  
glutInit() #inilisialisasi glut
glutInitDisplayMode(GLUT_RGBA) #mengatur layar supaya memunculkan warna 
glutInitWindowSize(600, 500) #untuk mengatur ukuran window
glutInitWindowPosition(200, 0) #untuk mengaatur posisi layar atau window untuk workspace 
wind = glutCreateWindow("Color Match") #untuk memberi nama pada window
timer1(0)
timer2(0)
timer3(0)
timer4(0)
timer5(0)
timer6(0)
timer7(0)
timer8(0)
timer9(0)
timer10(0)
glutDisplayFunc(showScreen) #untuk menampilkan object yang telah dibuat pada layar, fungsi callback
glutIdleFunc(showScreen) #membuat opengl terbuka dan menampilkan objek
glutMouseFunc(iniHandleMouse)
glutMainLoop() #untuk menilai segalanya dan untuk looping objek