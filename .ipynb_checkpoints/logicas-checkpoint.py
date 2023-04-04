def calcular_beneficio_integracion(Precio_KG_Res_Gorda_n12, Precio_KG_Res_Flaca_n,Peso_Inicial_Res_n,Por_Beneficio_Integrado,Peso_Final_Res_n12,Gasto_Operativo_Anual,Cantidad_Reses,Gasto_Transporte,Tasa_Costo_Capital,Cantidad_Reses_Simular):
    
    Peso_Final_Merma = Peso_Final_Res_n12 * 0.935
    Valor_Res_Flaca_Inversion = Precio_KG_Res_Flaca_n * Peso_Inicial_Res_n * Cantidad_Reses_Simular
    Valor_Res_Gorda = Precio_KG_Res_Gorda_n12*Peso_Final_Res_n12 * Cantidad_Reses_Simular
    Valor_Res_Gorda_con_Merma = Precio_KG_Res_Gorda_n12*Peso_Final_Merma * Cantidad_Reses_Simular
    Utilidad_Bruta =Valor_Res_Gorda_con_Merma- Valor_Res_Flaca_Inversion  
    Costo_Servicio_Finca = Por_Beneficio_Integrado * (Valor_Res_Gorda-Valor_Res_Flaca_Inversion)
    Gasto_Operativo = Gasto_Operativo_Anual/Cantidad_Reses
    Utilidad_Neta=Utilidad_Bruta-Costo_Servicio_Finca-Gasto_Operativo-Gasto_Transporte
    Impuesto= 0.3 * Utilidad_Neta
    Gasto_Transporte_Total = Gasto_Transporte * Cantidad_Reses_Simular
    UODI = Utilidad_Neta-Impuesto
    ROIC = UODI / Valor_Res_Flaca_Inversion
    Costo_Capital = Tasa_Costo_Capital *Valor_Res_Flaca_Inversion
    EVA = UODI -Costo_Capital

    Costo_Res_Integrada = Valor_Res_Flaca_Inversion +Costo_Servicio_Finca+Gasto_Operativo+Impuesto+Gasto_Transporte_Total+Costo_Capital
    Costo_Res_IntegradaKG =Costo_Res_Integrada/Peso_Final_Merma

    Beneficio = (Precio_KG_Res_Gorda_n12*Cantidad_Reses_Simular-Costo_Res_IntegradaKG)/(Precio_KG_Res_Gorda_n12*Cantidad_Reses_Simular)
    Beneficio_Integración = (Precio_KG_Res_Gorda_n12*Cantidad_Reses_Simular-Costo_Res_IntegradaKG)
    
    return(Beneficio,Valor_Res_Flaca_Inversion,UODI,Valor_Res_Gorda,ROIC, Utilidad_Neta,EVA,Costo_Capital)
    