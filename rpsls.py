#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��⽭
���ڣ�2020/4/14
"""
import random
# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����
def name_to_number(choice_name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if choice_name=="ʯͷ":
	    return 0
    elif choice_name=="ʷ����": 
	    return 1
    elif choice_name=="��":
	    return 2
    elif choice_name=="����":
	    return 3
    elif choice_name=="����":
	    return 4
    else:
        return 5    
    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
def number_to_name(comp_number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if comp_number==0:
      return "ʯͷ"
    elif comp_number==1:
      return "ʷ����"
    elif comp_number==2:
      return "��"
    elif comp_number==3:
      return "����"
    elif comp_number==4:
      return "����"
    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
def rpsls(choice_name):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    player_choice=name_to_number(choice_name)
    # �û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
    if player_choice==5:
      print("Error: No Correct Name")
    else:
      print("����ѡ��Ϊ��%s"%(choice_name))
    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
      comp_number=random.randint(0,4)
    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number
      player_choice_number=number_to_name(comp_number)	
    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����
      print("������ѡ��Ϊ��%s"%(player_choice_number))
    # ����Ļ����ʾ�����ѡ����������
      rule=comp_number-player_choice 
      if rule==2 or rule==-3 or rule==1 or rule==-4:
        print("����Ӯ��")
      elif rule==0:
        print("�����������һ����")
      else:
        print("��Ӯ��")  
    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�
    # �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
rpsls(choice_name)
