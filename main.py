from application import *
import dummy

@Application.run
def main():
    dummyEntity = Application.EntityManager.getEntity('DummyEntity')
    print(dummyEntity.getDummy())
