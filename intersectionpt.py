class Solution:
    
    def intersetPoint(self,head1,head2):
        #code here
        temp1=head1
        temp2=head2
        count1=0
        count2=0
        while temp1:
            count1+=1
            temp1=temp1.next
        while temp2:
            count2+=1
            temp2=temp2.next
        diff=abs(count1-count2)
        if count1>count2:
            temp1=head1
            for i in range(0,diff):
                temp1=temp1.next
            temp2=head2
        else:
            temp2=head2
            for i in range(0,diff):
                temp2=temp2.next
            temp1=head1
        
        while temp1!=temp2:
            temp1=temp1.next
            temp2=temp2.next
        return temp1.data   