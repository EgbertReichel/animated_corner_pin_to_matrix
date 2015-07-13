def CP2MTX():
    import nuke
    import nukescripts
    
    try:
        input = nuke.selectedNode()
    
        #----------------------------------------------------------------------------------------------------------
 
        if  input.Class() == 'CornerPin2D':
          
            node_in = input.input(0)
            
            cp = nuke.nodes.CornerPin2D( name = 'CornerPin_to_Matrix')
            
            xpos = input['xpos'].value()
            ypos = input['ypos'].value()
            
            cp_width = cp.screenWidth()
            cp_height = cp.screenHeight()
            
            cp.setXYpos(int(xpos) + int(cp_width) + 25 , int(ypos))
            cp.knob('extra matrix').setValue(True)
            cp.setInput(0, node_in)
            nuke.show(cp)
            cp_em = cp.knob('transform_matrix')
 
 
            #--------------------------------''' Define Frame Range'''---------------------------------    
    
            frames = nuke.getFramesAndViews('get FrameRange', '%s-%s' % (nuke.root().firstFrame(), nuke.root().lastFrame()))
            frame_range = nuke.FrameRange( frames[0] ) 
                    
            for i in frame_range:
 
                # conversion cp_to_mtx
                
                def getCPasMTX(cp):
                    projectionMatrixTo = nuke.math.Matrix4()
                    projectionMatrixFrom = nuke.math.Matrix4()
                        
                    imageWidth = float(cp.width())
                    imageHeight = float(cp.height())
                        
                    to1x = cp['to1'].getValueAt(i)[0]
                    to1y = cp['to1'].getValueAt(i)[1]
                    to2x = cp['to2'].getValueAt(i)[0]
                    to2y = cp['to2'].getValueAt(i)[1]
                    to3x = cp['to3'].getValueAt(i)[0]
                    to3y = cp['to3'].getValueAt(i)[1]
                    to4x = cp['to4'].getValueAt(i)[0]
                    to4y = cp['to4'].getValueAt(i)[1]
                        
                    from1x = cp['from1'].getValueAt(i)[0]
                    from1y = cp['from1'].getValueAt(i)[1]
                    from2x = cp['from2'].getValueAt(i)[0]
                    from2y = cp['from2'].getValueAt(i)[1]
                    from3x = cp['from3'].getValueAt(i)[0]
                    from3y = cp['from3'].getValueAt(i)[1]
                    from4x = cp['from4'].getValueAt(i)[0]
                    from4y = cp['from4'].getValueAt(i)[1]
                        
                        
                    projectionMatrixTo.mapUnitSquareToQuad(to1x,to1y,to2x,to2y,to3x,to3y,to4x,to4y)
                    projectionMatrixFrom.mapUnitSquareToQuad(from1x,from1y,from2x,from2y,from3x,from3y,from4x,from4y)
                        
                    mtx = projectionMatrixTo*projectionMatrixFrom.inverse()    
                    mtx.transpose()
                        
                    return mtx
                    
                #---------------------------------------------------------------------------------------
                
                mtx = getCPasMTX(input)
                              
                #------------------------------------------------------------------------------
                #apply values
                
                cp_em.setAnimated()
                for j in range(16):
                    cp_em.setValueAt(mtx[j], i, j )
                                                       
                                   
                #-----------------------------------------------------------------------------------------------    
            
 
        
        else:
    
            nuke.message('please select a CornerPin node')
     
    except:
 
         nuke.message('please select a CornerPin node')
     
     
#end script