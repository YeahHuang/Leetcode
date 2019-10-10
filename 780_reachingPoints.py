class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        #WA1: python的dfs深度限制还挺明显的
        if tx==sx and ty==sy:
            return True
        if tx < sx or ty < sy:
            return False
        if tx>ty:
            return self.reachingPoints(sx, sy, tx-ty, ty)
        else:
            return self.reachingPoints(sx,sy, tx, ty-tx)
        '''
        flag = False
        while tx>=sx and ty>=sy:
            if tx == sx and ty == sy:
                flag = True
                break
            if tx==0 or ty == 0:
                break
            if tx > ty:#直接除就是了 其实不用判断大小的 参考⬇️
                #tx -= ty
                tx %= ty
                if tx < sx and ty == sy and (sx-tx)%ty == 0:#WA2 一开始直接tx%=ty 一不小心就tx < sx了 没判断
                    tx = sx
            else:
                #ty -= tx
                ty %= tx
                if ty < sy and tx==sx and (sy-ty)%tx == 0:
                    ty = sy
        return flag

    #Improved: 简练很多  @lee215 
    def reachingPoints(self, sx, sy, tx, ty):
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx 
        return sx == tx and sy <= ty and (ty - sy) % sx == 0 or \
               sy == ty and sx <= tx and (tx - sx) % sy == 0    #最后这样一起弄一弄也还挺酷的吖 