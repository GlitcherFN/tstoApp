from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from core.vendor.tsto.tsto import TSTO
import json

core_tsto = TSTO()

def index(request):
  if not core_tsto.mLogined:
    return HttpResponseRedirect('/login')

  donuts = core_tsto.doLoadCurrency()

  if core_tsto.mLandMessage.id == '':
    core_tsto.doLandDownload()

  return render_to_response(
    'index.html',
    {
      'name': core_tsto.mLandMessage.friendData.name,
      'user': core_tsto.mUserId,
      'donuts': donuts.vcBalance,
      'data': core_tsto.mLandMessage.userData
    },
    context_instance=RequestContext(request)
  )

def item(request):
  if not core_tsto.mLogined:
    return HttpResponseRedirect('/login')

  if core_tsto.mLandMessage.id == '':
    core_tsto.doLandDownload()

  return render_to_response(
    'item.html',
    {
      'name': core_tsto.mLandMessage.friendData.name,
    },
    context_instance=RequestContext(request)
  )

def login(request):
  return render_to_response(
    'login.html',
    {},
    context_instance=RequestContext(request)
  )

def auth(request):
  if request.POST:
    user = request.POST['username']
    psw = request.POST['password']
    try:
      core_tsto.doAuth(['', user, psw])
      if core_tsto.mLogined:
        return HttpResponseRedirect('/')
    except Exception, e:
      print 'Error: ', e

  return HttpResponseRedirect('/login/')

def add_item(request):
  if not core_tsto.mLogined:
    return HttpResponseRedirect('/login')

  if core_tsto.mLandMessage.id == '':
    core_tsto.doLandDownload()

  return render_to_response(
    'add.html',
    {
      'name': core_tsto.mLandMessage.friendData.name,
    },
    context_instance=RequestContext(request)
  )

def add_donuts(request):
  status = 200
  if request.is_ajax():
    quantity = request.POST['add_donuts']
    try:
      core_tsto.doLandDownload()
      core_tsto.donutsAdd(['', quantity])
      core_tsto.doLandUpload()
    except Exception, e:
      print 'Error: ', e
      status = 500

    dataReturn = {
      'status': status
    }

    return HttpResponse(json.dumps(dataReturn), content_type='application/json')
  else:
    return HttpResponseRedirect('/')

def add_cash(request):
  status = 200
  if request.is_ajax():
    quantity = request.POST['add_cash']
    try:
      core_tsto.doLandDownload()
      core_tsto.moneySet(['', quantity])
      core_tsto.doLandUpload()
    except Exception, e:
      print 'Error: ', e
      status = 500

    dataReturn = {
      'status': status
    }

    return HttpResponse(json.dumps(dataReturn), content_type='application/json')
  else:
    return HttpResponseRedirect('/')

def set_xp(request):
  status = 200
  if request.is_ajax():
    quantity = request.POST['add_level']
    try:
      core_tsto.doLandDownload()
      core_tsto.levelSet(['', quantity])
      core_tsto.doLandUpload()
    except Exception, e:
      print 'Error: ', e
      status = 500

    dataReturn = {
      'status': status
    }

    return HttpResponse(json.dumps(dataReturn), content_type='application/json')
  else:
    return HttpResponseRedirect('/')

def add_spendable(request):
  status = 200
  if request.is_ajax():
    amount = request.POST['amount']
    types = request.POST['type']
    try:
      core_tsto.doLandDownload()
      core_tsto.spendableAdd(['', types, amount])
      core_tsto.doLandUpload()
    except Exception, e:
      print 'Spendable error: ', e
      status = 500

    dataReturn = {
      'status': status
    }

    return HttpResponse(json.dumps(dataReturn), content_type='application/json')
  else:
    return HttpResponseRedirect('/')